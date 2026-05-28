# 📊 Data Visualization — Group Project

A full-stack Data Science & Web application built by a 5-person team.

---

## 🏗️ Monorepo Structure

```
GroupProject/
├── frontend/               # ReactJS Web Dashboard (UI/UX, Time Slider, Custom Map)
│   ├── public/
│   ├── src/
│   │   ├── components/     # Reusable UI components (TimeSlider, MapView, Charts)
│   │   ├── pages/          # Route-level page components
│   │   ├── hooks/          # Custom React hooks
│   │   ├── services/       # API client & SignalR connection
│   │   ├── store/          # State management (Redux / Zustand)
│   │   └── utils/          # Utility/helper functions
│   ├── .env.example
│   └── package.json
│
├── backend/                # ASP.NET Core Web API
│   ├── src/
│   │   ├── Controllers/    # REST API controllers
│   │   ├── Hubs/           # SignalR hubs (real-time streaming)
│   │   ├── Models/         # Domain / EF Core entity models
│   │   ├── Services/       # Business logic & Background Services
│   │   ├── Data/           # DbContext, migrations, seeders
│   │   └── DTOs/           # Data Transfer Objects
│   ├── appsettings.json
│   ├── appsettings.Development.json
│   └── backend.csproj
│
├── ml_service/             # Python FastAPI — ML inference service
│   ├── app/
│   │   ├── api/            # FastAPI routers / endpoint definitions
│   │   ├── core/           # Config, settings, startup events
│   │   ├── models/         # Pydantic request/response schemas
│   │   └── services/       # Model loading & inference logic
│   ├── tests/              # Unit & integration tests
│   ├── .env.example
│   ├── main.py             # FastAPI application entry point
│   └── requirements.txt
│
├── data_workspace/         # Jupyter Notebooks, datasets & model artifacts
│   ├── notebooks/
│   │   ├── 01_EDA/         # Exploratory Data Analysis
│   │   ├── 02_feature_engineering/
│   │   └── 03_model_training/
│   ├── data/
│   │   ├── raw/            # Original, immutable source data
│   │   └── processed/      # Cleaned & feature-engineered data
│   ├── models/             # Serialized model artifacts (.pkl, .onnx)
│   └── requirements.txt
│
├── docs/                   # Project documentation
│   ├── architecture/       # Architecture diagrams (C4, system design)
│   ├── api_contracts/      # OpenAPI / Swagger YAML specs
│   └── meeting_notes/      # Sprint notes & decisions
│
├── .gitignore
└── README.md               # ← You are here
```

---

## 👥 Team Roles

| Member | Primary Responsibility                              |
| ------ | --------------------------------------------------- |
| 1      | Frontend — ReactJS Dashboard, Map & Time Slider     |
| 2      | Frontend — Charts, State Management, SignalR client |
| 3      | Backend — ASP.NET Core API, SignalR Hub, EF Core    |
| 4      | ML Service — FastAPI, Model Serving, Inference API  |
| 5      | Data — EDA, Feature Engineering, Model Training     |

---

## 🚀 Quick Start

### Frontend

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

### Backend

```bash
cd backend
dotnet restore
dotnet run
```

### ML Service

```bash
cd ml_service
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload --port 8000
```

### Data Workspace

```bash
cd data_workspace
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

---

## 🔗 Service Ports (Development)

| Service                | URL                        |
| ---------------------- | -------------------------- |
| React Dev Server       | http://localhost:5173      |
| ASP.NET Core API       | http://localhost:5000      |
| FastAPI ML Service     | http://localhost:8000      |
| FastAPI Docs (Swagger) | http://localhost:8000/docs |

---

## 📄 Documentation

See the [`docs/`](./docs/) directory for:

- Architecture diagrams
- API contracts (OpenAPI specs)
- Meeting notes & design decisions
