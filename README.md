# Airline_Data_CI_CD_Project
Airline data processing on GCP using Github actions, Airflow , Spark and BigQuery

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 650">
  <!-- Background -->
  <rect width="1000" height="650" fill="#f5f5f5"/>
  
  <!-- Title -->
  <text x="500" y="30" font-family="Arial" font-size="24" text-anchor="middle" font-weight="bold">Flight Booking Data Processing Architecture</text>
  
  <!-- GitHub Actions -->
  <rect x="50" y="80" width="120" height="60" rx="10" ry="10" fill="#6f42c1" stroke="#333" stroke-width="2"/>
  <text x="110" y="115" font-family="Arial" font-size="14" text-anchor="middle" fill="white">GitHub Actions</text>
  
  <!-- GCS Bucket -->
  <rect x="250" y="80" width="120" height="60" rx="10" ry="10" fill="#4285F4" stroke="#333" stroke-width="2"/>
  <text x="310" y="115" font-family="Arial" font-size="14" text-anchor="middle" fill="white">GCS Bucket</text>
  
  <!-- Cloud Composer (Airflow) -->
  <rect x="450" y="80" width="120" height="60" rx="10" ry="10" fill="#EA4335" stroke="#333" stroke-width="2"/>
  <text x="510" y="115" font-family="Arial" font-size="14" text-anchor="middle" fill="white">Cloud Composer</text>
  
  <!-- Flight Booking Data -->
  <rect x="250" y="200" width="120" height="60" rx="10" ry="10" fill="#4285F4" stroke="#333" stroke-width="2"/>
  <text x="310" y="235" font-family="Arial" font-size="14" text-anchor="middle" fill="white">Flight Booking Data</text>
  
  <!-- Airflow DAG -->
  <rect x="450" y="200" width="120" height="60" rx="10" ry="10" fill="#EA4335" stroke="#333" stroke-width="2"/>
  <text x="510" y="235" font-family="Arial" font-size="14" text-anchor="middle" fill="white">Airflow DAG</text>
  
  <!-- File Sensor -->
  <rect x="450" y="320" width="120" height="60" rx="10" ry="10" fill="#EA4335" stroke="#333" stroke-width="2"/>
  <text x="510" y="355" font-family="Arial" font-size="14" text-anchor="middle" fill="white">File Sensor</text>
  
  <!-- Cluster Creation - NEW -->
  <rect x="450" y="440" width="120" height="60" rx="10" ry="10" fill="#EA4335" stroke="#333" stroke-width="2"/>
  <text x="510" y="475" font-family="Arial" font-size="14" text-anchor="middle" fill="white">Cluster Creation</text>
  
  <!-- Dataproc Cluster -->
  <rect x="650" y="440" width="120" height="60" rx="10" ry="10" fill="#0F9D58" stroke="#333" stroke-width="2"/>
  <text x="710" y="475" font-family="Arial" font-size="14" text-anchor="middle" fill="white">Dataproc Cluster</text>
  
  <!-- PySpark Job -->
  <rect x="650" y="560" width="120" height="60" rx="10" ry="10" fill="#0F9D58" stroke="#333" stroke-width="2"/>
  <text x="710" y="595" font-family="Arial" font-size="14" text-anchor="middle" fill="white">PySpark Job</text>
  
  <!-- BigQuery Tables -->
  <rect x="850" y="560" width="120" height="60" rx="10" ry="10" fill="#FBBC05" stroke="#333" stroke-width="2"/>
  <text x="910" y="595" font-family="Arial" font-size="14" text-anchor="middle" fill="white">BigQuery Tables</text>
  
  <!-- Cluster Deletion -->
  <rect x="650" y="320" width="120" height="60" rx="10" ry="10" fill="#EA4335" stroke="#333" stroke-width="2"/>
  <text x="710" y="355" font-family="Arial" font-size="14" text-anchor="middle" fill="white">Cluster Deletion</text>
  
  <!-- Arrows -->
  <!-- GitHub Actions to GCS -->
  <path d="M170 110 L250 110" fill="none" stroke="#333" stroke-width="2" stroke-dasharray="5,5"/>
  <polygon points="245,105 250,110 245,115" fill="#333"/>
  
  <!-- GitHub Actions to Cloud Composer -->
  <path d="M170 110 C210 110 210 110 210 110 L 210 60 C 210 60 350 60 350 60 L 350 110 C 350 110 450 110 450 110" fill="none" stroke="#333" stroke-width="2" stroke-dasharray="5,5"/>
  <polygon points="445,105 450,110 445,115" fill="#333"/>
  
  <!-- GCS to Flight Booking Data -->
  <path d="M310 140 L310 200" fill="none" stroke="#333" stroke-width="2"/>
  <polygon points="305,195 310,200 315,195" fill="#333"/>
  
  <!-- Cloud Composer to Airflow DAG -->
  <path d="M510 140 L510 200" fill="none" stroke="#333" stroke-width="2"/>
  <polygon points="505,195 510,200 515,195" fill="#333"/>
  
  <!-- Airflow DAG to File Sensor -->
  <path d="M510 260 L510 320" fill="none" stroke="#333" stroke-width="2"/>
  <polygon points="505,315 510,320 515,315" fill="#333"/>
  
  <!-- File Sensor to Cluster Creation -->
  <path d="M510 380 L510 440" fill="none" stroke="#333" stroke-width="2"/>
  <polygon points="505,435 510,440 515,435" fill="#333"/>
  
  <!-- Cluster Creation to Dataproc Cluster -->
  <path d="M570 470 L650 470" fill="none" stroke="#333" stroke-width="2"/>
  <polygon points="645,465 650,470 645,475" fill="#333"/>
  
  <!-- Dataproc Cluster to PySpark Job -->
  <path d="M710 500 L710 560" fill="none" stroke="#333" stroke-width="2"/>
  <polygon points="705,555 710,560 715,555" fill="#333"/>
  
  <!-- PySpark Job to BigQuery -->
  <path d="M770 590 L850 590" fill="none" stroke="#333" stroke-width="2"/>
  <polygon points="845,585 850,590 845,595" fill="#333"/>
  
  <!-- Flight Booking Data to File Sensor -->
  <path d="M310 260 L310 350 L450 350" fill="none" stroke="#333" stroke-width="2"/>
  <polygon points="445,345 450,350 445,355" fill="#333"/>
  
  <!-- PySpark Job to Cluster Deletion -->
  <path d="M710 560 C780 560 800 450 780 380 C760 320 710 320 710 320" fill="none" stroke="#333" stroke-width="2"/>
  <polygon points="710,325 710,320 715,320" fill="#333"/>
  
  <!-- Legend -->
  <rect x="50" y="590" width="20" height="20" fill="#6f42c1"/>
  <text x="80" y="605" font-family="Arial" font-size="12">CI/CD</text>
  
  <rect x="150" y="590" width="20" height="20" fill="#4285F4"/>
  <text x="180" y="605" font-family="Arial" font-size="12">Storage</text>
  
  <rect x="250" y="590" width="20" height="20" fill="#EA4335"/>
  <text x="280" y="605" font-family="Arial" font-size="12">Orchestration</text>
  
  <rect x="400" y="590" width="20" height="20" fill="#0F9D58"/>
  <text x="430" y="605" font-family="Arial" font-size="12">Processing</text>
  
  <rect x="550" y="590" width="20" height="20" fill="#FBBC05"/>
  <text x="580" y="605" font-family="Arial" font-size="12">Analytics</text>
  
  <rect x="700" y="590" width="20" height="20" fill="none" stroke="#333" stroke-width="2" stroke-dasharray="5,5"/>
  <text x="730" y="605" font-family="Arial" font-size="12">Deployment</text>
  
  <rect x="850" y="590" width="20" height="20" fill="none" stroke="#333" stroke-width="2"/>
  <text x="880" y="605" font-family="Arial" font-size="12">Data Flow</text>
</svg>

I'll update the diagram to include the explicit Dataproc cluster creation step that occurs after the file sensor detects a file.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 650">
  <!-- Background -->
  <rect width="1000" height="650" fill="#f5f5f5"/>
  
  <!-- Title -->
  <text x="500" y="30" font-family="Arial" font-size="24" text-anchor="middle" font-weight="bold">Flight Booking Data Processing Architecture</text>
  
  <!-- GitHub Actions -->
  <rect x="50" y="80" width="120" height="60" rx="10" ry="10" fill="#6f42c1" stroke="#333" stroke-width="2"/>
  <text x="110" y="115" font-family="Arial" font-size="14" text-anchor="middle" fill="white">GitHub Actions</text>
  
  <!-- GCS Bucket -->
  <rect x="250" y="80" width="120" height="60" rx="10" ry="10" fill="#4285F4" stroke="#333" stroke-width="2"/>
  <text x="310" y="115" font-family="Arial" font-size="14" text-anchor="middle" fill="white">GCS Bucket</text>
  
  <!-- Cloud Composer (Airflow) -->
  <rect x="450" y="80" width="120" height="60" rx="10" ry="10" fill="#EA4335" stroke="#333" stroke-width="2"/>
  <text x="510" y="115" font-family="Arial" font-size="14" text-anchor="middle" fill="white">Cloud Composer</text>
  
  <!-- Flight Booking Data -->
  <rect x="250" y="200" width="120" height="60" rx="10" ry="10" fill="#4285F4" stroke="#333" stroke-width="2"/>
  <text x="310" y="235" font-family="Arial" font-size="14" text-anchor="middle" fill="white">Flight Booking Data</text>
  
  <!-- Airflow DAG -->
  <rect x="450" y="200" width="120" height="60" rx="10" ry="10" fill="#EA4335" stroke="#333" stroke-width="2"/>
  <text x="510" y="235" font-family="Arial" font-size="14" text-anchor="middle" fill="white">Airflow DAG</text>
  
  <!-- File Sensor -->
  <rect x="450" y="320" width="120" height="60" rx="10" ry="10" fill="#EA4335" stroke="#333" stroke-width="2"/>
  <text x="510" y="355" font-family="Arial" font-size="14" text-anchor="middle" fill="white">File Sensor</text>
  
  <!-- Cluster Creation - NEW -->
  <rect x="450" y="440" width="120" height="60" rx="10" ry="10" fill="#EA4335" stroke="#333" stroke-width="2"/>
  <text x="510" y="475" font-family="Arial" font-size="14" text-anchor="middle" fill="white">Cluster Creation</text>
  
  <!-- Dataproc Cluster -->
  <rect x="650" y="440" width="120" height="60" rx="10" ry="10" fill="#0F9D58" stroke="#333" stroke-width="2"/>
  <text x="710" y="475" font-family="Arial" font-size="14" text-anchor="middle" fill="white">Dataproc Cluster</text>
  
  <!-- PySpark Job -->
  <rect x="650" y="560" width="120" height="60" rx="10" ry="10" fill="#0F9D58" stroke="#333" stroke-width="2"/>
  <text x="710" y="595" font-family="Arial" font-size="14" text-anchor="middle" fill="white">PySpark Job</text>
  
  <!-- BigQuery Tables -->
  <rect x="850" y="560" width="120" height="60" rx="10" ry="10" fill="#FBBC05" stroke="#333" stroke-width="2"/>
  <text x="910" y="595" font-family="Arial" font-size="14" text-anchor="middle" fill="white">BigQuery Tables</text>
  
  <!-- Cluster Deletion -->
  <rect x="650" y="320" width="120" height="60" rx="10" ry="10" fill="#EA4335" stroke="#333" stroke-width="2"/>
  <text x="710" y="355" font-family="Arial" font-size="14" text-anchor="middle" fill="white">Cluster Deletion</text>
  
  <!-- Arrows -->
  <!-- GitHub Actions to GCS -->
  <path d="M170 110 L250 110" fill="none" stroke="#333" stroke-width="2" stroke-dasharray="5,5"/>
  <polygon points="245,105 250,110 245,115" fill="#333"/>
  
  <!-- GitHub Actions to Cloud Composer -->
  <path d="M170 110 C210 110 210 110 210 110 L 210 60 C 210 60 350 60 350 60 L 350 110 C 350 110 450 110 450 110" fill="none" stroke="#333" stroke-width="2" stroke-dasharray="5,5"/>
  <polygon points="445,105 450,110 445,115" fill="#333"/>
  
  <!-- GCS to Flight Booking Data -->
  <path d="M310 140 L310 200" fill="none" stroke="#333" stroke-width="2"/>
  <polygon points="305,195 310,200 315,195" fill="#333"/>
  
  <!-- Cloud Composer to Airflow DAG -->
  <path d="M510 140 L510 200" fill="none" stroke="#333" stroke-width="2"/>
  <polygon points="505,195 510,200 515,195" fill="#333"/>
  
  <!-- Airflow DAG to File Sensor -->
  <path d="M510 260 L510 320" fill="none" stroke="#333" stroke-width="2"/>
  <polygon points="505,315 510,320 515,315" fill="#333"/>
  
  <!-- File Sensor to Cluster Creation -->
  <path d="M510 380 L510 440" fill="none" stroke="#333" stroke-width="2"/>
  <polygon points="505,435 510,440 515,435" fill="#333"/>
  
  <!-- Cluster Creation to Dataproc Cluster -->
  <path d="M570 470 L650 470" fill="none" stroke="#333" stroke-width="2"/>
  <polygon points="645,465 650,470 645,475" fill="#333"/>
  
  <!-- Dataproc Cluster to PySpark Job -->
  <path d="M710 500 L710 560" fill="none" stroke="#333" stroke-width="2"/>
  <polygon points="705,555 710,560 715,555" fill="#333"/>
  
  <!-- PySpark Job to BigQuery -->
  <path d="M770 590 L850 590" fill="none" stroke="#333" stroke-width="2"/>
  <polygon points="845,585 850,590 845,595" fill="#333"/>
  
  <!-- Flight Booking Data to File Sensor -->
  <path d="M310 260 L310 350 L450 350" fill="none" stroke="#333" stroke-width="2"/>
  <polygon points="445,345 450,350 445,355" fill="#333"/>
  
  <!-- PySpark Job to Cluster Deletion -->
  <path d="M710 560 C780 560 800 450 780 380 C760 320 710 320 710 320" fill="none" stroke="#333" stroke-width="2"/>
  <polygon points="710,325 710,320 715,320" fill="#333"/>
  
  <!-- Legend -->
  <rect x="50" y="590" width="20" height="20" fill="#6f42c1"/>
  <text x="80" y="605" font-family="Arial" font-size="12">CI/CD</text>
  
  <rect x="150" y="590" width="20" height="20" fill="#4285F4"/>
  <text x="180" y="605" font-family="Arial" font-size="12">Storage</text>
  
  <rect x="250" y="590" width="20" height="20" fill="#EA4335"/>
  <text x="280" y="605" font-family="Arial" font-size="12">Orchestration</text>
  
  <rect x="400" y="590" width="20" height="20" fill="#0F9D58"/>
  <text x="430" y="605" font-family="Arial" font-size="12">Processing</text>
  
  <rect x="550" y="590" width="20" height="20" fill="#FBBC05"/>
  <text x="580" y="605" font-family="Arial" font-size="12">Analytics</text>
  
  <rect x="700" y="590" width="20" height="20" fill="none" stroke="#333" stroke-width="2" stroke-dasharray="5,5"/>
  <text x="730" y="605" font-family="Arial" font-size="12">Deployment</text>
  
  <rect x="850" y="590" width="20" height="20" fill="none" stroke="#333" stroke-width="2"/>
  <text x="880" y="605" font-family="Arial" font-size="12">Data Flow</text>
</svg>

```

# Workflow Explanation


1. **CI/CD Process**:
   - GitHub Actions triggers when code is pushed to dev or main branch
   - Deploys code artifacts to GCS bucket
   - Updates Airflow variables in Cloud Composer

2. **Data Ingestion**:
   - Flight booking data is stored in GCS
   - Organized in environment-specific folders (dev/prod)

3. **Orchestration & Monitoring**:
   - Cloud Composer (Airflow) manages the workflow
   - The Airflow DAG includes a file sensor that monitors for new data files

4. **Cluster Management**:
   - When a new file is detected, Airflow first triggers the Cluster Creation task
   - This task provisions a new Dataproc cluster with the appropriate specifications
   - The cluster is created with the necessary configurations for running the PySpark job

5. **Processing**:
   - Once the cluster is available, Airflow submits the PySpark job
   - The job processes the flight booking data:
     - Applies transformations (weekend flag, lead time categories, etc.)
     - Generates route-based insights
     - Analyzes bookings by origin

6. **Data Loading**:
   - The PySpark job writes processed data directly to BigQuery tables:
     - Main transformed data table
     - Route insights table
     - Origin insights table

7. **Cleanup**:
   - After the PySpark job completes, Airflow triggers the cluster deletion task
   - This ensures cost optimization by removing the cluster when it's no longer needed.