
import re
import streamlit as st

st.set_page_config(
    page_title="Molar Mass Calculator",
    page_icon="🧪",
    layout="centered",
)

# Atomic masses: standard atomic weights where available;
# representative mass numbers for elements without standard weights.
ELEMENTS = {
    "H": ("Hydrogen", 1.008), "He": ("Helium", 4.0026),
    "Li": ("Lithium", 6.94), "Be": ("Beryllium", 9.0122),
    "B": ("Boron", 10.81), "C": ("Carbon", 12.011),
    "N": ("Nitrogen", 14.007), "O": ("Oxygen", 15.999),
    "F": ("Fluorine", 18.998), "Ne": ("Neon", 20.180),
    "Na": ("Sodium", 22.990), "Mg": ("Magnesium", 24.305),
    "Al": ("Aluminium", 26.982), "Si": ("Silicon", 28.085),
    "P": ("Phosphorus", 30.974), "S": ("Sulfur", 32.06),
    "Cl": ("Chlorine", 35.45), "Ar": ("Argon", 39.948),
    "K": ("Potassium", 39.0983), "Ca": ("Calcium", 40.078),
    "Sc": ("Scandium", 44.9559), "Ti": ("Titanium", 47.867),
    "V": ("Vanadium", 50.9415), "Cr": ("Chromium", 51.9961),
    "Mn": ("Manganese", 54.938), "Fe": ("Iron", 55.845),
    "Co": ("Cobalt", 58.9332), "Ni": ("Nickel", 58.6934),
    "Cu": ("Copper", 63.546), "Zn": ("Zinc", 65.38),
    "Ga": ("Gallium", 69.723), "Ge": ("Germanium", 72.630),
    "As": ("Arsenic", 74.9216), "Se": ("Selenium", 78.971),
    "Br": ("Bromine", 79.904), "Kr": ("Krypton", 83.798),
    "Rb": ("Rubidium", 85.4678), "Sr": ("Strontium", 87.62),
    "Y": ("Yttrium", 88.9058), "Zr": ("Zirconium", 91.224),
    "Nb": ("Niobium", 92.9064), "Mo": ("Molybdenum", 95.95),
    "Tc": ("Technetium", 98), "Ru": ("Ruthenium", 101.07),
    "Rh": ("Rhodium", 102.9055), "Pd": ("Palladium", 106.42),
    "Ag": ("Silver", 107.8682), "Cd": ("Cadmium", 112.414),
    "In": ("Indium", 114.818), "Sn": ("Tin", 118.710),
    "Sb": ("Antimony", 121.760), "Te": ("Tellurium", 127.60),
    "I": ("Iodine", 126.9045), "Xe": ("Xenon", 131.293),
    "Cs": ("Caesium", 132.9055), "Ba": ("Barium", 137.327),
    "La": ("Lanthanum", 138.9055), "Ce": ("Cerium", 140.116),
    "Pr": ("Praseodymium", 140.9077), "Nd": ("Neodymium", 144.242),
    "Pm": ("Promethium", 145), "Sm": ("Samarium", 150.36),
    "Eu": ("Europium", 151.964), "Gd": ("Gadolinium", 157.25),
    "Tb": ("Terbium", 158.9254), "Dy": ("Dysprosium", 162.500),
    "Ho": ("Holmium", 164.9303), "Er": ("Erbium", 167.259),
    "Tm": ("Thulium", 168.9342), "Yb": ("Ytterbium", 173.045),
    "Lu": ("Lutetium", 174.9668), "Hf": ("Hafnium", 178.49),
    "Ta": ("Tantalum", 180.9479), "W": ("Tungsten", 183.84),
    "Re": ("Rhenium", 186.207), "Os": ("Osmium", 190.23),
    "Ir": ("Iridium", 192.217), "Pt": ("Platinum", 195.084),
    "Au": ("Gold", 196.9666), "Hg": ("Mercury", 200.592),
    "Tl": ("Thallium", 204.38), "Pb": ("Lead", 207.2),
    "Bi": ("Bismuth", 208.9804), "Po": ("Polonium", 209),
    "At": ("Astatine", 210), "Rn": ("Radon", 222),
    "Fr": ("Francium", 223), "Ra": ("Radium", 226),
    "Ac": ("Actinium", 227), "Th": ("Thorium", 232.0377),
    "Pa": ("Protactinium", 231.0359), "U": ("Uranium", 238.0289),
    "Np": ("Neptunium", 237), "Pu": ("Plutonium", 244),
    "Am": ("Americium", 243), "Cm": ("Curium", 247),
    "Bk": ("Berkelium", 247), "Cf": ("Californium", 251),
    "Es": ("Einsteinium", 252), "Fm": ("Fermium", 257),
    "Md": ("Mendelevium", 258), "No": ("Nobelium", 259),
    "Lr": ("Lawrencium", 266), "Rf": ("Rutherfordium", 267),
    "Db": ("Dubnium", 268), "Sg": ("Seaborgium", 269),
    "Bh": ("Bohrium", 270), "Hs": ("Hassium", 269),
    "Mt": ("Meitnerium", 278), "Ds": ("Darmstadtium", 281),
    "Rg": ("Roentgenium", 282), "Cn": ("Copernicium", 285),
    "Nh": ("Nihonium", 286), "Fl": ("Flerovium", 289),
    "Mc": ("Moscovium", 290), "Lv": ("Livermorium", 293),
    "Ts": ("Tennessine", 294), "Og": ("Oganesson", 294),
}

ATOMIC_MASSES = {
    symbol: details[1] for symbol, details in ELEMENTS.items()
}


def parse_formula(formula):
    """Parse chemical formulas with nested round parentheses."""
    tokens = re.findall(r"[A-Z][a-z]?|\d+|[()]", formula)

    if not tokens or "".join(tokens) != formula:
        raise ValueError(
            "Invalid formula. Check element symbols and formatting."
        )

    def parse_group(index, nested=False):
        counts = {}

        while index < len(tokens):
            token = tokens[index]

            if token == ")":
                if not nested:
                    raise ValueError(
                        "Closing parenthesis has no matching opening parenthesis."
                    )
                return counts, index + 1

            if token == "(":
                inner_counts, index = parse_group(index + 1, nested=True)
                multiplier = 1

                if index < len(tokens) and tokens[index].isdigit():
                    multiplier = int(tokens[index])
                    index += 1

                if multiplier < 1:
                    raise ValueError("Subscripts must be positive integers.")

                for symbol, amount in inner_counts.items():
                    counts[symbol] = (
                        counts.get(symbol, 0) + amount * multiplier
                    )
                continue

            if token.isdigit():
                raise ValueError(
                    "A number must follow an element or closing parenthesis."
                )

            symbol = token

            if symbol not in ELEMENTS:
                raise ValueError(
                    f"Element '{symbol}' is not in the database."
                )

            index += 1
            amount = 1

            if index < len(tokens) and tokens[index].isdigit():
                amount = int(tokens[index])
                index += 1

            if amount < 1:
                raise ValueError("Subscripts must be positive integers.")

            counts[symbol] = counts.get(symbol, 0) + amount

        if nested:
            raise ValueError(
                "Opening parenthesis has no matching closing parenthesis."
            )

        return counts, index

    counts, end_index = parse_group(0)

    if end_index != len(tokens) or not counts:
        raise ValueError("Please check the chemical formula.")

    return counts


def calculate_molar_mass(formula):
    counts = parse_formula(formula)
    breakdown = []
    total_mass = 0.0

    for symbol, atom_count in counts.items():
        element_name = ELEMENTS[symbol][0]
        atomic_mass = ATOMIC_MASSES[symbol]
        contribution = atomic_mass * atom_count
        total_mass += contribution

        breakdown.append({
            "Symbol": symbol,
            "Element": element_name,
            "Number of atoms": atom_count,
            "Atomic mass (g/mol)": atomic_mass,
            "Contribution (g/mol)": round(contribution, 4),
        })

    return total_mass, breakdown


# ---------- APP INTERFACE ----------

st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 2.25rem;
        font-weight: 750;
        margin-bottom: 0.25rem;
    }
    .subtitle {
        text-align: center;
        color: #777;
        margin-bottom: 1.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="main-title">🧪 Molar Mass Calculator</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="subtitle">Calculate the molar mass of a compound in seconds.</div>',
    unsafe_allow_html=True,
)

st.divider()

st.markdown("### Enter a chemical formula")

with st.form("molar_mass_form"):
    formula = st.text_input(
        "Chemical formula",
        placeholder="e.g. H2O, CO2, Ca(OH)2",
        help="Use correct element symbols and numbers for subscripts.",
    )

    submitted = st.form_submit_button(
        "Calculate molar mass",
        type="primary",
        use_container_width=True,
    )

st.caption(
    "Try: H2O · CO2 · NaCl · Ca(OH)2 · Al2(SO4)3 · KMnO4"
)

if submitted:
    if not formula.strip():
        st.warning("Please enter a chemical formula first.")
    else:
        try:
            molar_mass, breakdown = calculate_molar_mass(formula.strip())

            st.success(f"Calculation complete for {formula.strip()}!")
            st.metric("Molar Mass", f"{molar_mass:.3f} g/mol")

            st.markdown("### Element breakdown")
            st.dataframe(
                breakdown,
                use_container_width=True,
                hide_index=True,
            )

            st.caption(
                "For elements without standard atomic weights, representative "
                "mass numbers are used. Actual values can vary by isotope."
            )

        except ValueError as error:
            st.error(str(error))

with st.expander("About this calculator"):
    st.write(
        "This calculator includes all 118 element symbols and their names. "
        "It supports element counts and nested round parentheses."
    )
    st.write(
        "Hydrates, square brackets, ionic charges, and isotope-specific "
        "notation are not yet supported."
    )
    st.write(f"Elements included: {len(ELEMENTS)} / 118")

st.divider()
st.caption("Built for chemistry students · Python + Streamlit")
