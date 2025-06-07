
#  NGINX Load Balancer for Streamlit Apps on EC2

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:630/0*2qFWlICCcXc5Vz4Q.png" alt="Load balancer" />
</p>


This project demonstrates how to use **NGINX** as a * **load balancer** to serve multiple **Streamlit apps** running on an **EC2 instance**. Ideal for learning the basics of web servers, app deployment, and load balancing.

### 📁 Project Structure

```
.
├── app1.py
├── app2.py
├── requirements.txt
└── README.md
````

###  Prerequisites

- Ubuntu EC2 instance (`t2.micro` is enough for testing)
- NGINX installed (`sudo apt install nginx`)
- `Python 3` and `venv`
- Ports `80`, `8501`, `8502` open in your EC2 security group


## 🛠 Setup Instructions

#### 1. Create two simple Streamlit apps Check the files from the repo

#### 2. Set up a virtual environment and install Streamlit

```bash
python3 -m venv streamlit-env

source streamlit-env/bin/activate

pip install streamlit
```


#### 3. Run both Streamlit apps

```bash
# In one terminal
streamlit run app1.py --server.port 8501  --server.address 127.0.0.1

# In another terminal (or background)
streamlit run app2.py --server.port 8502  --server.address 127.0.0.1
```

#### 4. Configure NGINX as a load balancer

Create a config file (e.g., `/etc/nginx/sites-available/loadbalancer`) with the following:

```nginx
upstream backend_servers {
    server 127.0.0.1:8501;
    server 127.0.0.1:8502;
}

server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://backend_servers;
        proxy_http_version 1.1;

        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

#### 5. Enable the config and reload NGINX

```bash
sudo ln -s /etc/nginx/sites-available/loadbalancer /etc/nginx/sites-enabled/

sudo nginx -t  # Test config

sudo systemctl reload nginx
```

#### 6. Access Your App

Open your browser and visit:

```
http://<your-ec2-public-ip>
```

Refresh the page multiple times — you’ll see it switch between **App 1** and **App 2** 🎯 

<br>

<img width="956" alt="Screenshot 2025-06-08 at 1 03 46 AM" src="https://github.com/user-attachments/assets/d9f01900-4184-4a5c-9e14-3e7fd93efa1a" />

<br>

<img width="956" alt="Screenshot 2025-06-08 at 1 05 49 AM" src="https://github.com/user-attachments/assets/4c4b2e83-184b-496c-977e-43dcd67fe5d9" />

<br>


### 🧑‍💻 Author

**Raghul**  
Connect with me on [LinkedIn - Raghul-M](https://www.linkedin.com/in/m-raghul/) or explore my tech blog [blog.raghul.in/](https://blog.raghul.in/)



