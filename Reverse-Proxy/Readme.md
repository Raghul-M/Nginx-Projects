# Hosting Streamlit App on EC2 with NGINX Reverse Proxy

![Reverse Proxy](https://miro.medium.com/v2/resize:fit:1400/1*Gm_q3hi9cBRFeGA1NoxowQ.png)


This project demonstrates how to deploy a simple Streamlit app on an AWS EC2 instance and serve it using NGINX as a reverse proxy.
It enables accessing the app through standard HTTP port 80 instead of the default Streamlit port (8501).


## What is a Reverse Proxy?

A **reverse proxy** is a server that sits between clients (users) and your backend application server. It accepts requests from clients, forwards them to your app, and then returns the response back to the client.


## Why use a Reverse Proxy?

- **Security:** Hides your app’s internal details and port.
- **SSL Termination:** Handles HTTPS encryption for your app.
- **Load Balancing:** Distributes traffic if you have multiple instances.
- **URL Routing:** Allows multiple apps on the same server under different URLs or domains.
- **Performance:** Enables caching and compression.
- **Single Access Point:** Manage all traffic through one server.


## Example Scenario

- Streamlit app runs on `localhost:8501`.
- Reverse proxy (NGINX) listens on `http://yourdomain.com` or `http://server-ip`.
- NGINX forwards incoming requests to `localhost:8501` transparently.

---

### 1. Streamlit App Code (`app.py`)

```python
import streamlit as st

st.title("Hello from Streamlit on EC2!")
st.write("This is a simple app to test NGINX reverse proxy.")

name = st.text_input("Enter your name:")

if name:
    st.success(f"Welcome, {name}!")
```

### 2. Setup Python Virtual Environment and Install Streamlit

```bash
# Update package info and install venv if missing
sudo apt-get update
sudo apt-get install python3-venv -y

# Create a virtual environment in your home directory
python3 -m venv streamlit-env

# Activate the virtual environment
source streamlit-env/bin/activate

# Install Streamlit inside the venv
pip install streamlit
```


### 3. Run Streamlit App

```bash
streamlit run app.py --server.port 8501 --server.address 127.0.0.1
```

* `--server.address 127.0.0.1` restricts the app to listen only on localhost for security.
* Leave the terminal running or use `tmux`/`screen` for session persistence.


### 4. Configure NGINX Reverse Proxy

Create a new NGINX config file:

```bash
sudo nano /etc/nginx/sites-available/streamlit
```

Paste the following config:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;  # Replace with your domain or use _ for default

    location / {
        proxy_pass http://127.0.0.1:8501;
        proxy_http_version 1.1;

        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

Enable the site and disable default:

```bash
sudo ln -s /etc/nginx/sites-available/streamlit /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
```

Test and reload NGINX:

```bash
sudo nginx -t
sudo systemctl reload nginx
```



### 5. EC2 Security Group Settings

* Allow inbound traffic on port **80 (HTTP)** for web access.
* Allow inbound traffic on port **22 (SSH)** from your IP for management.
* Do **NOT** open port 8501 publicly.



### 6. Access Your App

* Visit `http://yourdomain.com` or `http://<your-ec2-public-ip>/` in your browser.
* You should see the Streamlit app served via NGINX.

#### You should see This Site

<img width="1397" alt="Screenshot 2025-06-08 at 12 29 27 AM" src="https://github.com/user-attachments/assets/c2c31500-8884-4fd7-88fb-539b2e25a6e5" />



## 7. Troubleshooting

* Make sure Streamlit app is running and listening on `127.0.0.1:8501`.
* Check NGINX config with `sudo nginx -t`.
* Restart NGINX if you make config changes: `sudo systemctl restart nginx`.
* Verify your domain DNS points correctly to your EC2 public IP.
* Clear browser cache or test with `curl`.



## Optional Enhancements

* Setup HTTPS using [Let's Encrypt](https://letsencrypt.org/) and `certbot`.
* Run Streamlit app as a systemd service for auto-start on reboot.
* Serve multiple apps with NGINX by configuring multiple server blocks.

---

### 🧑‍💻 Author

**Raghul**  
Connect with me on [LinkedIn - Raghul-M](https://www.linkedin.com/in/m-raghul/) or explore my tech blog [blog.raghul.in/](https://blog.raghul.in/)

