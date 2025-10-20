# Virtual Diabetes Clinic ML

The project aims to predict disease progression through machnine learning creating a risk score for patients. This is meant for usage from nurses to identify the patients that may need follow up evaluations based on their predicted risk score through their sampled data.

The project fetches the data with FastAPI and then packaged as a Container in Docker is then able to be used with systems that have the Docker Desktop application/program.

### Preconditions (What you need to run this) <br>
- Internet connection
- Docker Desktop instaled and running on your current device 
- The pc Terminal

## Testing ML API: 

### V0.1
docker pull ghcr.io/filipbelhaj/diabetesclinic3:v0.1

### V0.2
docker pull ghcr.io/filipbelhaj/diabetesclinic3:v0.2

## RUN:

### V0.1
docker run -p 8080:8080 ghcr.io/filipbelhaj/diabetesclinic3:v0.1

### V0.2
docker run -p 8080:8080 ghcr.io/filipbelhaj/diabetesclinic3:v0.2

## Check Health: 
http://localhost:8080/health

## PREDICT:
http://localhost:8080/docs

Sample Payload:

{ <br>
"age": 0.02, <br>
"sex": -0.044, <br>
"bmi": 0.06, <br>
"bp": -0.03, <br>
"s1": -0.02, <br>
"s2": 0.03, <br>
"s3": -0.02,<br>
"s4": 0.02, <br>
"s5": 0.02, <br>
"s6": -0.001 <br>
}

## Sample Response V0.1:

{<br>
  "prediction": 235.9496372217627,<br>
  "model_version": "v0.1"<br>
}

## Sample Response V0.2:

{<br>
  "prediction": 226.91314681729386,<br>
  "model_version": "v0.2",<br>
  "high_risk": true<br>
}

## VERSIONS
V0.1 Uses Linear Regression and StandardScaler as a baseline model <br>
V0.2 Is a improved model using Ridge regularization and risk calibration <br>


| Date (Day/Month-Year) | Description | Author | Status |
|------------------------|-------------|---------|---------|
| 20/10-2025 | Update Dockerfile – optimized image build and dependencies | filipbelhaj | ✅ Verified |
| 20/10-2025 | Update predict_service.py – improved model prediction logic | filipbelhaj | ✅ Verified |
| 20/10-2025 | Create README.md – added project documentation and setup guide | jeppesamuelsson | ✅ Verified |
| 20/10-2025 | Update predict_service.py – refactoring and minor bug fixes | filipbelhaj | ✅ Verified |
| 19/10-2025 | Update publish.yml – refined GitHub Actions workflow | filipbelhaj | ✅ Verified |
| 19/10-2025 | Update publish.yml – minor workflow adjustments | filipbelhaj | ✅ Verified |
| 19/10-2025 | Create publish.yml – initial publishing pipeline for container image | filipbelhaj | ✅ Verified |
| 19/10-2025 | Create release.yml – added release automation workflow | filipbelhaj | ✅ Verified |
| 19/10-2025 | Delete .github/workflows/release.yml – removed duplicate file | filipbelhaj | ✅ Verified |
| 19/10-2025 | Update ci.yml – updated continuous integration setup | filipbelhaj | ✅ Verified |
| 19/10-2025 | Create ci.yml – initial CI workflow for automated testing | filipbelhaj | ✅ Verified |
| 19/10-2025 | Create release.yml – setup release configuration | filipbelhaj | ✅ Verified |
| 19/10-2025 | Create .gitignore – added standard Python and Docker ignores | filipbelhaj | ✅ Verified |
| 19/10-2025 | Create .dockerignore – excluded unnecessary files from Docker build | filipbelhaj | ✅ Verified |
| 19/10-2025 | Add files via upload – initial project upload | filipbelhaj | ✅ Verified |

---

## Authors:
Filip Belhaj, Jesper Samuelsson, Samuel Petterson





