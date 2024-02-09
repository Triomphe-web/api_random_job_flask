from flask import Flask, jsonify
import random

app = Flask(__name__)

job_titles = ["Développeur Full Stack", "Ingénieur en IA", "Analyste financier", "Designer UX/UI", "Chef de projet IT", "Spécialiste en marketing numérique"]
companies = ["Entreprise A", "Entreprise B", "Entreprise C", "Entreprise D", "Entreprise E"]
locations = ["Paris", "Lyon", "Marseille", "Toulouse", "Bordeaux"]
salaries = ["50 000 €", "60 000 €", "45 000 €", "55 000 €", "70 000 €"]

def generate_jobs():
    jobs = []
    for _ in range(20):  # Générer exactement 20 offres d'emploi
        job = {
            'title': random.choice(job_titles),
            'company': random.choice(companies),
            'location': random.choice(locations),
            'salary': random.choice(salaries)
        }
        jobs.append(job)
    return jobs

@app.route('/')
def get_jobs():
    jobs = generate_jobs()
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)
