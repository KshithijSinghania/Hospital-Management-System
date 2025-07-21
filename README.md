<h1>🏥 Hospital Management System + 🧠 MediBot (AI Symptom Checker Chatbot)</h1>

<p>An integrated full-stack Hospital Management System built with the <strong>MERN stack (MongoDB, Express, React, Node.js)</strong>, enhanced by <strong>MediBot</strong>, an AI-powered chatbot that assists patients by checking symptoms and suggesting nearby hospitals.</p>

<hr />

<h2>🚀 Overview</h2>

<p>This web application streamlines hospital operations, including managing users (admins, doctors, patients), appointments, and medical records. It includes a smart chatbot, <strong>MediBot</strong>, that uses a PyTorch-trained model to provide preliminary symptom analysis and offline hospital recommendations based on location.</p>

<p>All components are combined into a single repository with three main folders:</p>

<ul>
  <li><code>backend</code> – Node.js + Express API</li>
  <li><code>frontend</code> – React-based UI</li>
  <li><code>chatbot</code> – Flask app with PyTorch model</li>
</ul>

<hr />

<h2>🔗 Live Demo</h2>

<ul>
  <li>🌐 <a href="https://hospital-management-system-six-pi.vercel.app/" target="_blank" rel="noopener noreferrer">Frontend (Vercel)</a></li>
  <li>🖥️ <a href="https://hospital-management-system-1dqr.onrender.com" target="_blank" rel="noopener noreferrer">Backend API (Render)</a></li>
  <li>🤖 <a href="https://hospital-management-system-chatbot.onrender.com" target="_blank" rel="noopener noreferrer">MediBot Chatbot (Render)</a></li>
</ul>

<hr />

<h2>✨ Features</h2>

<h3>🏥 Hospital Management System</h3>
<ul>
  <li>🔐 User authentication & authorization (Patients, Doctors, Admins)</li>
  <li>📅 Appointment scheduling & patient record management</li>
  <li>👨‍⚕️ Doctor dashboard with profile & availability</li>
  <li>📊 Admin dashboard to manage users & hospital data</li>
  <li>💻 Responsive UI for mobile and desktop</li>
</ul>

<h3>🤖 MediBot – AI Symptom Checker Chatbot</h3>
<ul>
  <li>🧠 Intent classification using a PyTorch model</li>
  <li>💬 Flask-powered chat interface embedded in the app</li>
  <li>📍 Offline hospital lookup by area (e.g., “Kilpauk”, “Adyar”)</li>
  <li>🧪 Terminal test version for debugging</li>
  <li>📁 Static dataset (no external API calls required)</li>
</ul>

<hr />

<h2>🛠️ Technologies Used</h2>

<h3>Frontend</h3>
<ul>
  <li>React</li>
  <li>React Router</li>
  <li>Tailwind CSS</li>
  <li>Lucide Icons</li>
  <li>Axios</li>
</ul>

<h3>Backend</h3>
<ul>
  <li>Node.js</li>
  <li>Express.js</li>
  <li>MongoDB & Mongoose</li>
  <li>JWT (JSON Web Token) for auth</li>
  <li>dotenv for environment config</li>
</ul>

<h3>Chatbot</h3>
<ul>
  <li>Python</li>
  <li>Flask</li>
  <li>PyTorch</li>
  <li>scikit-learn</li>
  <li>Jinja2</li>
</ul>

<hr />

<h2>⚙️ Getting Started (For Local Development)</h2>

<h3>📦 Prerequisites</h3>
<ul>
  <li>Node.js v14+</li>
  <li>Python 3.7+</li>
  <li>MongoDB (local or cloud)</li>
</ul>

<hr />

<h2>📁 Installation & Setup</h2>

<h3>1. Clone the Repository</h3>

<pre><code>git clone https://github.com/KshithijSinghania/Hospital-Management-System.git
cd Hospital-Management-System
</code></pre>

<h3>2. Setup Backend (Node.js/Express)</h3>

<pre><code>cd backend
npm install
</code></pre>

<p>Create a <code>.env</code> file in <code>backend</code>:</p>

<pre><code>MONGO_URI=mongodb://0.0.0.0/Hospital-Management-System-MERN
PORT=8080
</code></pre>

<p>Optionally, create the first admin by editing <code>createAdmin.js</code>:</p>

<pre><code>const admin = new Admin({
  firstName: "abc",
  lastName: "xyz",
  email: "abc@gmail.com",
  password: "xyz123",
  role: "admin"
});
</code></pre>

<pre><code>node createAdmin.js
node server.js
</code></pre>

<h3>3. Setup Frontend (React)</h3>

<pre><code>cd ../frontend
npm install
</code></pre>

<p>Create a <code>.env</code> file in <code>frontend</code>:</p>

<pre><code>REACT_APP_API_URL=https://your-backend-api.onrender.com
REACT_APP_CHATBOT_URL=https://your-chatbot-api.onrender.com
</code></pre>

<pre><code>npm start</code></pre>

<p>Visit: <a href="http://localhost:3000" target="_blank" rel="noopener noreferrer">http://localhost:3000</a></p>

<h3>4. Setup MediBot Chatbot (Flask)</h3>

<pre><code>cd ../chatbot
pip install -r requirements.txt
</code></pre>

<p>(Optional) To retrain the model:</p>

<pre><code>python model/train.py
</code></pre>

<pre><code>python app.py
</code></pre>

<p>Visit: <a href="http://127.0.0.1:5000" target="_blank" rel="noopener noreferrer">http://127.0.0.1:5000</a></p>

<hr />

<h2>🧪 Chatbot Test CLI (Optional)</h2>

<pre><code>python test_chat.py</code></pre>

<hr />

<h2>🧑‍💻 Contributing</h2>

<p>Contributions are welcome! Feel free to:</p>
<ul>
  <li>Submit a pull request 🛠️</li>
  <li>Open issues for bugs/suggestions 🐛</li>
  <li>Improve model training or expand the dataset 📊</li>
</ul>

<hr />

<h2>📄 License</h2>

<p>This project is open source and available under the <a href="LICENSE" target="_blank" rel="noopener noreferrer">MIT License</a>.</p>
