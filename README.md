# ChallengeApp
Challenge application flask

Challenge DevOps - Patrizio Ottaviani

Challenge: Automazione e CI/CD con Docker
La sfida consiste nel creare un'applicazione containerizzata utilizzando Docker e configurare un'intera pipeline CI/CD automatizzata. La pipeline dovrà includere l'integrazione continua (CI) per eseguire test e la distribuzione continua (CD) per rilasciare automaticamente l'applicazione su un ambiente di produzione (ad esempio Kubernetes o un server Docker). Utilizzerai strumenti come GitHub Actions, Jenkins, GitLab CI o altri strumenti di CI/CD, con il supporto di Docker.

Requisiti:
	1. Linguaggio: Puoi utilizzare qualsiasi linguaggio di programmazione per la tua applicazione (ad esempio, Node.js, Python, Go, Java).
	2. Docker: La tua applicazione deve essere containerizzata e includere un file Dockerfile per la costruzione dell'immagine.
	3. Automazione: Configura una pipeline di automazione che esegua la Build dell'applicazione utilizzando un Dockerfile per creare un'immagine container della tua applicazione.
		-Esecuzione di test automatizzati: Integra unit test o test end-to-end come parte del processo di build.
		-Creazione e push dell’immagine Docker: Dopo aver superato i test, l'immagine Docker dovrà essere pushata in un registry (Docker Hub, GitLab Registry, ECR, ecc.).
	4. Continuous Deployment: Una volta che l'immagine è stata creata e pushata, la pipeline deve distribuire automaticamente l'applicazione in una macchina Docker.
	5. Monitoraggio e Verifica: Implementa un sistema di monitoraggio o notifiche, in modo che in caso di fallimenti, tu riceva un avviso (ad es. integrazione con Slack, email, webhook). Verifica che la pipeline sia completamente automatizzata e funzioni dall'inizio alla fine senza intervento manuale.

Obiettivi opzionali:

	1. Blue/Green Deployment o Canary Release: Implementa una strategia di deployment avanzata come il Blue/Green Deployment o il Canary Release.
	2. Test End-to-End (E2E): Aggiungi test end-to-end alla pipeline per garantire che tutte le funzionalità dell'applicazione funzionino correttamente.
	3. Scalabilità: Configura il deploy su un cluster Kubernetes o Docker Swarm e scala l'applicazione automaticamente in base al carico.
	4. Security Scanning: Aggiungi alla pipeline un controllo di sicurezza per analizzare vulnerabilità nei container Docker.

L’applicazione dovrà essere containerizzata e funzionare correttamente.
La pipeline  dovrà  coprire tutte le fasi (build, test, push dell’immagine, deploy) e  dovrà  distribuire automaticamente la nuova versione dell'applicazione al termine della build.
I test dovranno coprire le funzionalità principali dell'applicazione.

Le Tecnologie Suggerite:
	-CI/CD Tools: GitHub Actions, GitLab CI, Jenkins, CircleCI
	-Container Registry: Docker Hub, GitLab Container Registry
	-Orchestrazione: Kubernetes, Docker Swarm
	-Monitoraggio: Prometheus, Grafana, Slack Notifications
