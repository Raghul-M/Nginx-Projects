# NGINX Static Website Hosting 

<p align="center">
  <img src="https://github.com/user-attachments/assets/fa92b23c-5d39-453a-b071-b7d086d744e3" alt="image" />
</p>


This project demonstrates how to host a simple static HTML website using **NGINX** on an Ubuntu server.

## What You'll Learn

- How to install and configure NGINX
- How to serve a static site using NGINX
- Understanding NGINX configuration files
- Basics of systemd services and permissions

## 🛠️ Setup Steps

### 1.  Install NGINX

```bash
sudo apt update
sudo apt install nginx -y
```

### 2.  Create a Static Website

```bash
sudo mkdir -p /var/www/mysite
```

Create an `index.html`:

```bash
sudo nano /var/www/mysite/index.html
```

Paste the sample content from inex.html :



### 3. Create NGINX Config File

Create a new config file:

```bash
sudo nano /etc/nginx/sites-available/mysite
```

Paste this configuration:

```nginx
server {
    listen 80;
    server_name yourdomain.com;  # Or use your public IP / localhost if no domain

    root /var/www/mysite;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

### 4. Enable the Site

```bash
sudo ln -s /etc/nginx/sites-available/mysite /etc/nginx/sites-enabled/
```

### 5. Test and Restart NGINX

```bash
sudo nginx -t
sudo systemctl reload nginx
```

##  Access Your Site


Open your server IP in the browser:  
`http://<your-server-ip>` or `http://localhost`

**You should see This Site** 

![Screenshot 2025-05-20 at 12 46 54 AM](https://github.com/user-attachments/assets/e1dcdadc-664c-4caa-b1f3-c2cf7b4aa95e)

## 📂 Folder Structure

```
/var/www/mysite
├── index.html
/etc/nginx/
├── sites-available/
│   └── mysite
├── sites-enabled/
    └── mysite -> ../sites-available/mysite
```


## 📌 Notes

- No domain name is needed for basic hosting (use your server IP or localhost ).
- If you are using EC2 instance make sure to enable indbound rules for these ports 80, 443 , 22
- Use `systemctl status nginx` to check if NGINX is running.



## 🧑‍💻 Author

**Raghul**  
Connect with me on [LinkedIn - Raghul-M](https://www.linkedin.com/in/m-raghul/) or explore my tech blog [blog.raghul.in/](https://blog.raghul.in/)
