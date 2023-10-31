
# Deployment Guide: Docker and Google Cloud Platform (GCP) 🚀

Radhe Radhe, dost! 🙏 Kaise hain aap? Aaj toh tyohaar ka din hai, aur hum yahaan ek aur tyohaar manaane ja rahe hain — apne project ko deploy karke! Chaliye, shuru karte hain!

## Docker ke saath Chalu Karein 🐳

### Step 1: Docker Install Karein 🛠️

Agar Docker pehle se install nahi hua hai toh [yahaan se download karein](https://www.docker.com/products/docker-desktop).

### Step 2: Dockerfile Banayein 📝

Project ke root directory mein ek `Dockerfile` naam ki file banayein, aur usmein yeh code daalein:

```Dockerfile
FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
```

### Step 3: Docker Image Banayein 🖼️

Command prompt ya terminal kholein, aur type karein:

```bash
docker build -t my-awesome-app .
```

### Step 4: Docker Container Run Karein 🏃

Ab, type karein:

```bash
docker run -p 5000:5000 my-awesome-app
```

## Google Cloud Platform (GCP) pe Le Jaayein ☁️

### Step 1: GCP Console 🖥️

[GCP Console](https://console.cloud.google.com/) pe jaayein aur ek naya project create karein.

### Step 2: Google Cloud SDK Install Karein 🛠️

Agar Google Cloud SDK install nahi hua hai toh [yahaan se download karein](https://cloud.google.com/sdk).

### Step 3: Project Deploy Karein 🚀

Terminal mein, type karein:

```bash
gcloud app deploy
```

Aur follow karein on-screen instructions.

Radhe Radhe! Aapne toh kamal kar diya! Ab aapka app live hai. Tyohaar ki tarah khushiyaan baantein! 🎉
