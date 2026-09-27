# ✈️ TripMate AI — Autonomous Multi-Agent Travel Planner

<img width="1310" height="669" alt="Screenshot (763)" src="https://github.com/user-attachments/assets/37c86394-8ed0-4861-942a-33dd3a6903ec" />


<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/FastAPI-0.136%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/LangGraph-1.2%2B-FF6F00?style=for-the-badge&logo=langchain&logoColor=white" alt="LangGraph" />
  <img src="https://img.shields.io/badge/Groq-LPU%20Inference-F05032?style=for-the-badge&logoColor=white" alt="Groq" />
  <img src="https://img.shields.io/badge/PostgreSQL-Checkpointer-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
</p>

---

## 🌟 Overview

**TripMate AI** is a production-grade, autonomous travel planning application powered by a **LangGraph multi-agent orchestration architecture**. It transforms simple, natural-language travel prompts (e.g., *"Plan a 7-day Japan trip from Bangladesh under 2 lakhs"*) into structured, end-to-end itineraries complete with real-time flight schedules, verified hotel options, day-by-day activity schedules, budget breakdowns, and downloadable PDF travel vouchers.

Built with **FastAPI**, **LangChain**, **Groq LPU inference**, and **PostgreSQL state checkpointers**, TripMate AI models complex travel planning into specialized, collaborative agent nodes that guarantee grounded and actionable outputs.

---

## 🚀 Key Features

- **🧠 Multi-Agent Orchestration**: Graph-based pipeline using `LangGraph` separating flight discovery, hotel search, itinerary generation, and response synthesis into dedicated nodes.
- **✈️ Live Flight Intelligence**: Intelligently resolves city/country names to **IATA airport codes** via `airportsdata` & `pycountry`, fetching scheduled departures, terminals, gates, and statuses via the **AviationStack API**.
- **🏨 Real-Time Hotel Discovery**: Curates localized accommodations and stay options using the **Tavily AI Search API**.
- **⚡ Ultra-Fast LLM Generation**: Powered by **Groq** (`openai/gpt-oss-120b`) for near-instant reasoning and itinerary synthesis.
- **💾 Stateful Conversation Checkpointing**: Backed by PostgreSQL (`PostgresSaver`) to retain conversation history and enable contextual multi-turn planning across threads.
- **🎨 Glassmorphic Earth-Tone UI**: Styled with a responsive **Olive + Mustard + Cream** aesthetic featuring micro-animations, quick-prompt pills, and real-time Markdown rendering via `marked.js`.
- **📄 Instant PDF & Clipboard Export**: Export itineraries directly to formatted PDF files with `html2pdf.js` or copy full Markdown with one click.
- **🐳 Containerized & Cloud Ready**: Fully Dockerized for seamless deployment on Render, Railway, AWS, or local environments.

---

## 🏗️ Multi-Agent Architecture

TripMate AI executes planning tasks through a directed acyclic state graph (`StateGraph`). Each agent performs specialized retrieval or synthesis before passing enriched state to subsequent nodes:

```mermaid
flowchart TD
    START([User Prompt]) --> FlightAgent["✈️ Flight Agent<br/>(IATA Parser + AviationStack)"]
    FlightAgent --> HotelAgent["🏨 Hotel Agent<br/>(Tavily Search API)"]
    HotelAgent --> ItineraryAgent["📅 Itinerary Agent<br/>(Groq LLM Reasoning)"]
    ItineraryAgent --> FinalAgent["📝 Final Response Agent<br/>(Structured Formatter)"]
    FinalAgent --> END([Structured Response & PDF])

    subgraph StatePersistence["💾 Persistence Layer"]
        DB[(PostgreSQL Checkpointer)] -.->|Thread State Checkpoint| FlightAgent
        DB -.->|Thread State Checkpoint| HotelAgent
        DB -.->|Thread State Checkpoint| ItineraryAgent
        DB -.->|Thread State Checkpoint| FinalAgent
    end
```

### Agent Breakdown

1. **Flight Agent (`flight_agent`)**:
   - Parses natural-language departure and arrival points using rule-based and country/city alias dictionaries.
   - Resolves IATA codes (e.g., `Dhaka` ➡️ `DAC`, `Japan` ➡️ `NRT`).
   - Fetches live flights, scheduled arrival/departure times, terminals, and delays from AviationStack.
2. **Hotel Agent (`hotel_agent`)**:
   - Queries Tavily Search for top-rated, budget-appropriate hotels and accommodations matching the target destination.
3. **Itinerary Agent (`itinerary_agent`)**:
   - Synthesizes flight availability and hotel recommendations into a logical, day-by-day travel schedule.
4. **Final Response Agent (`final_agent`)**:
   - Formats the complete plan into 6 standardized sections:
     1. **Trip Summary**
     2. **Flight Information**
     3. **Hotel Suggestions**
     4. **Day-by-Day Itinerary**
     5. **Estimated Budget Breakdown**
     6. **Final Practical Travel Tips**

---
<img width="1294" height="686" alt="Screenshot (764)" src="https://github.com/user-attachments/assets/60a5f331-faef-442a-b6cc-605839e4d47c" />
<img width="1292" height="679" alt="Screenshot (765)" src="https://github.com/user-attachments/assets/bdfa3218-6b8b-4725-8cc0-a873f670acba" />
<img width="1250" height="680" alt="Screenshot (766)" src="https://github.com/user-attachments/assets/77936c01-38bd-40d5-9b91-94fd4f3a796a" />

## 🧰 Tech Stack

| Domain | Technology / Library | Purpose |
|---|---|---|
| **Backend Framework** | [FastAPI](https://fastapi.tiangolo.com/) + [Uvicorn](https://www.uvicorn.org/) | High-performance asynchronous API & static file server |
| **Agent Framework** | [LangGraph](https://github.com/langchain-ai/langgraph) & [LangChain](https://github.com/langchain-ai/langchain) | State machine graph coordination & prompt templating |
| **LLM Provider** | [Groq](https://groq.com/) (`openai/gpt-oss-120b`) | High-speed LLM inference |
| **State Persistence** | [PostgreSQL](https://www.postgresql.org/) + `psycopg[binary]` | Thread-safe conversation checkpointing (`PostgresSaver`) |
| **Flight Intelligence** | [AviationStack API](https://aviationstack.com/) + `airportsdata` + `pycountry` | Live route parsing and flight telemetry |
| **Web Research** | [Tavily Search API](https://tavily.com/) | Real-time web retrieval for hotels and accommodations |
| **Frontend UI** | HTML5, Vanilla CSS, JavaScript, [Jinja2](https://jinja.palletsprojects.com/) | Responsive glassmorphic interface (Olive/Mustard/Cream theme) |
| **Frontend Libraries** | [marked.js](https://marked.js.org/) & [html2pdf.js](https://ekoopmans.github.io/html2pdf.js/) | Markdown rendering and client-side PDF generation |
| **Containerization** | Docker | Production container image |

---

## 📁 Repository Structure

```text
TripMate/
├── app.py                  # FastAPI application entry point & API route definitions
├── backend.py              # LangGraph state graph definition & Postgres checkpointer
├── requirements.txt        # Pinned Python package dependencies
├── DockerFile              # Docker container build specifications
├── test.py                 # Interactive terminal/CLI testing script
├── static/
│   ├── script.js           # Client-side API caller, Markdown rendering & PDF downloader
│   └── style.css           # Glassmorphism design system (Olive, Mustard & Cream theme)
├── templates/
│   └── index.html          # Main travel planner interactive web interface
└── tools/
    ├── __init__.py         # Package marker
    ├── flight_tool.py      # Route parsing, IATA resolution & AviationStack client
    └── tavily_tool.py      # Tavily search tool for hotel & accommodation retrieval
```

---

## ⚙️ Environment Variables

Create a `.env` file in the root of the project with the following keys:

```env
# ------------------------------------------------------------------------------
# DATABASE SETTINGS
# ------------------------------------------------------------------------------
# PostgreSQL connection string for LangGraph checkpointing (Local or Cloud e.g. Render/Supabase)
DATABASE_URL=postgresql://username:password@localhost:5432/travel_db

# ------------------------------------------------------------------------------
# AI & SEARCH API KEYS
# ------------------------------------------------------------------------------
# Groq API key for LLM generation
GROQ_API_KEY=gsk_your_groq_api_key_here

# Tavily API key for hotel research
TAVILY_API_KEY=tvly-your_tavily_api_key_here

# AviationStack API key for flight lookups
AVIATIONSTACK_API_KEY=your_aviationstack_api_key_here

# ------------------------------------------------------------------------------
# DEFAULT DEPARTURE CONFIGURATION
# ------------------------------------------------------------------------------
# Default IATA code if no origin is specified in user query (Default: DAC for Dhaka)
DEFAULT_ORIGIN_IATA=DAC
```

---

## 🛠️ Installation & Setup

### Prerequisites

- **Python 3.10+** installed
- **PostgreSQL** instance running locally or hosted (e.g., Render, Neon, Supabase)
- Valid API keys for **Groq**, **Tavily**, and **AviationStack**

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/TripMate.git
cd TripMate
```

### 2. Set Up a Virtual Environment

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create your `.env` file from the template shown above:
```bash
cp .env.example .env   # Or create .env manually and populate with your keys
```

---

## 🏃 Running the Application

### Option A: Start the FastAPI Web Server

```bash
python app.py
```
Or with Uvicorn directly:
```bash
uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

Once started, navigate to:
👉 **`http://127.0.0.1:8000/`**

### Option B: Run in CLI Mode (Quick Test)

You can run queries interactively from your terminal using `test.py`:
```bash
python test.py
```
Enter your prompt when prompted (e.g. `Plan a 5-day Dubai trip from Dhaka`).

---

## 🐳 Docker Deployment

Build and run TripMate AI in a self-contained container:

### 1. Build the Docker Image
```bash
docker build -t tripmate-ai .
```

### 2. Run the Container
```bash
docker run -d \
  -p 8000:8000 \
  --name tripmate-app \
  --env-file .env \
  tripmate-ai
```

The application will be accessible at `http://localhost:8000`.

---

## 📡 API Reference

### 1. Health Check
```http
GET /health
```
**Response (`200 OK`):**
```json
{
  "status": "ok",
  "message": "AI Travel Planner API is running"
}
```

---

### 2. Generate Travel Plan
```http
POST /api/travel
Content-Type: application/json
```

**Request Body:**
```json
{
  "message": "Plan a complete 7 days Japan trip from Bangladesh under 2 lakhs.",
  "thread_id": "optional-thread-uuid"
}
```

**Response (`200 OK`):**
```json
{
  "success": true,
  "thread_id": "user_a1b2c3d4e5f6...",
  "answer": "# Trip Summary\n\n...",
  "flight_results": "Live flights from DAC to NRT...",
  "hotel_results": "Title: Tokyo Luxury Hotel...",
  "itinerary": "Day 1: Arrival in Tokyo...",
  "llm_calls": 4
}
```

#### Example cURL Request:
```bash
curl -X POST "http://127.0.0.1:8000/api/travel" \
  -H "Content-Type: application/json" \
  -d '{"message": "Plan a 4 days trip to Singapore with budget stays"}'
```

---

## 💡 Troubleshooting & Notes

- **Database SSL Mode**: If you are using Render, Supabase, or AWS RDS, PostgreSQL requires SSL connections. The application automatically appends `sslmode=require` if omitted from `DATABASE_URL`.
- **Flight Pricing Disclaimer**: The **AviationStack** free tier provides live telemetry (status, gates, scheduled arrival/departure) rather than dynamic ticket pricing. The LLM estimates ticket cost ranges in the budget summary accordingly.
- **SSL Certificate Verification**: For Windows systems or restricted corporate networks, `certifi` is loaded into `SSL_CERT_FILE` and `REQUESTS_CA_BUNDLE` automatically in `backend.py` and `flight_tool.py`.

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](file:///e:/TripMate/TripMate/LICENSE) for more information.
