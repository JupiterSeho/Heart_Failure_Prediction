## Welcome ! Here is what you have to know.

As part of this project, we have successively:
- Developed a machine learning model capable of predicting whether or not an individual is likely to suffer a heart attack.
- Created an API based on this model, and put it into production.
- Then monitor certain metrics by displaying dashboards using the Prometheus/Grafana tandem.


To run this project locally, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/votre-utilisateur/votre-projet.git
    cd votre-projet
    ```

2. Build the Docker image:

    ```bash
    docker build -t facial-emotion-recognition .
    ```

3. Launch the Docker containers for FastAPI, Prometheus, and Grafana:

    ```bash
    docker-compose up -d
    ```

4. Open your browser and navigate to the following URLs:

   - FastAPI: [http://localhost:5000](http://localhost:5000)
   - Prometheus: [http://localhost:9090](http://localhost:9090)
   - Grafana: [http://localhost:3000](http://localhost:3000)

5. In Grafana, you can view the pre-built dashboards or create your own.

    - Log in to Grafana with the default credentials (username: admin, password: grafana).
    - Explore the dashboards to monitor various metrics related to the machine learning model.

Feel free to customize the instructions based on the specifics of your project and the structure of your repository.
