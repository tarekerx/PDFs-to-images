# PDF to PNG Converter

Converts all PDF files in the `input/` folder to PNG images, saved in `output/`.

---

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2. Install Poppler (required by pdf2image)

| OS | Command |
|----|---------|
| **Windows** | Download from [poppler-windows](https://github.com/oschwartz10612/poppler-windows/releases) and add `bin/` to your PATH |
| **macOS** | `brew install poppler` |
| **Linux** | `sudo apt install poppler-utils` |

### 3. Create and activate a virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Python dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

1. Place your PDF files inside the `input/` folder
2. Run the script:
```bash
python main.py
```
3. Find your PNGs in the `output/` folder

### Output naming
- Single-page PDF → `filename.png`
- Multi-page PDF → `filename_page1.png`, `filename_page2.png`, ...

### Change resolution
Edit the `DPI` value at the top of `main.py`:
```python
DPI = 200  # 300 for print quality, 150 for smaller file size
```

---

## Project Structure

```
project/
├── main.py            # Main script
├── requirements.txt   # Python dependencies
├── .gitignore         # Git ignore rules
├── README.md          # This file
├── input/             # Put your PDFs here (not tracked by git)
└── output/            # PNGs will be saved here (not tracked by git)
```
