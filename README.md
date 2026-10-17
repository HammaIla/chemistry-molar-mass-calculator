# 🧪 Chemistry Molar Mass Calculator

A lightweight, interactive chemistry web application that calculates the molar mass of chemical compounds from their molecular formulas.

Built with **Python** and **Streamlit**, this project is designed to help chemistry students perform molar mass calculations quickly and understand how each element contributes to the total.

## 🚀 Live Demo

**Try the application:** https://chemistry-molar-mass-calculator.streamlit.app/

## ✨ Features

- **118 elements:** Includes all 118 recognized chemical elements in its element database.
- **Molar mass calculation:** Calculates the molar mass of a compound in grams per mole (g/mol).
- **Element breakdown:** Displays each element's symbol, name, atom count, atomic mass, and contribution to the total.
- **Parentheses support:** Handles chemical formulas containing groups and nested parentheses.
- **Formula validation:** Provides helpful error messages for invalid formulas and unsupported element symbols.
- **Interactive interface:** Offers a simple, browser-based experience powered by Streamlit.
- **Educational purpose:** Helps students understand the relationship between chemical formulas, atomic masses, and molar mass.

## 🧪 Example Calculations

| Chemical formula | Compound | Approximate molar mass |
|---|---|---:|
| `H2O` | Water | 18.015 g/mol |
| `CO2` | Carbon dioxide | 44.009 g/mol |
| `NaCl` | Sodium chloride | 58.440 g/mol |
| `Ca(OH)2` | Calcium hydroxide | 74.092 g/mol |
| `Al2(SO4)3` | Aluminium sulfate | 342.131 g/mol |
| `KMnO4` | Potassium permanganate | 158.032 g/mol |

*Values depend on the atomic masses used in the application's database.*

## 🛠️ Technologies Used

- **Python** — calculation logic and formula parsing
- **Streamlit** — interactive web interface
- **Regular expressions** — chemical formula tokenization
- **Git and GitHub** — version control and project hosting
- **Streamlit Community Cloud** — web deployment

## 💻 Run Locally

### Prerequisites

- Python installed on your computer
- Git (optional, for cloning the repository)

### 1. Clone the repository

```bash
git clone https://github.com/HammaIla/chemistry-molar-mass-calculator.git
```

### 2. Enter the project directory

```bash
cd chemistry-molar-mass-calculator
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run main.py
```

Streamlit will provide a local URL, usually `http://localhost:8501`, where you can open the calculator in your browser.

## 📁 Project Structure

```text
chemistry-molar-mass-calculator/
├── main.py             # Application and calculation logic
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## ⚗️ How It Works

1. The user enters a chemical formula, such as `Ca(OH)2`.
2. The application tokenizes the formula into element symbols, numerical subscripts, and parentheses.
3. The parser determines the number of atoms of each element, including atoms inside parenthesized groups.
4. The application retrieves the corresponding atomic masses from its element database.
5. It multiplies each atomic mass by the number of atoms and adds the contributions together.
6. The total molar mass and element-by-element breakdown are displayed.

The calculation follows the relationship:

**Molar mass = Σ (number of atoms × atomic mass)**

## ⚠️ Current Limitations

The current version supports element symbols, numerical subscripts, and round parentheses, including nested groups.

The following features are not yet supported:

- Hydrate notation, such as `CuSO4·5H2O`
- Square brackets and braces in complex formulas
- Ionic charges and electron-mass corrections
- Isotope-specific notation
- Advanced chemical formula validation

For elements without a standard atomic weight, the database uses representative mass numbers. Actual isotopic masses may differ.

## 🗺️ Future Improvements

Potential future enhancements include:

- A complete interactive periodic table
- Formula support for hydrates and complex bracket notation
- Molar mass calculations for isotope-specific formulas
- Exportable calculation reports
- Improved formula validation and unit options
- Automated tests for calculation accuracy

## 🤝 Contributing

Contributions, bug reports, and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make and test your changes.
4. Submit a pull request describing your contribution.

Please verify calculation accuracy and formula parsing when modifying the application.

## 📄 License

No license has been specified yet. Until a license is added to the repository, reuse and redistribution permissions are not explicitly granted.

## 👨‍💻 Author

**Ismail Labaran Ibrahim**

Chemistry student and aspiring software developer exploring the intersection of science and technology.

---

*Built to make chemistry calculations more accessible to students and learners.*
