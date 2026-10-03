# LegalEase

AI-Powered Legal Document Generator built from the supplied project specification.

## Structure

- `frontend/app.py` — Streamlit UI
- `backend/main.py` — FastAPI server
- `backend/routes.py` — API routes
- `ai_core/gemini_generator.py` — Gemini integration + local fallback
- `services/document_service.py` — TXT/DOCX/PDF generation

## Windows setup

Open the folder in VS Code, then run:

```powershell
.\setup.bat
```

Or manually:

```powershell
py -3 -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

If `venv` is already active, do not create another virtual environment inside it.

## Run backend

```powershell
.\venv\Scripts\Activate.ps1
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs` to test the API.

## Run frontend

Open a second terminal:

```powershell
.\venv\Scripts\Activate.ps1
python -m streamlit run frontend\app.py
```

## Gemini

Put your key in `.env`:

```text
GEMINI_API_KEY=YOUR_KEY_HERE
GEMINI_MODEL=gemini-3.8-flash
```

If the key is blank or the online AI call fails, LegalEase automatically uses its built-in local draft generator, so the app can still run.

## Test

```powershell
python test_project.py
```

Expected output:

`LegalEase self-test: PASS`

Generated documents are drafts and should be reviewed by a qualified legal professional before real-world use.
