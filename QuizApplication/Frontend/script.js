const API_URL = 'http://127.0.0.1:8000';

const App = {
    state: {
        user: JSON.parse(localStorage.getItem('quiz_user')) || null
    },

    async api(endpoint, method = 'GET', data = null) {
        const url = `${API_URL}${endpoint}`;
        const options = {
            method,
            headers: { 'Content-Type': 'application/json' }
        };
        if (data) options.body = JSON.stringify(data);

        try {
            const response = await fetch(url, options);
            if (!response.ok) throw new Error('API Error');
            return await response.json();
        } catch (error) {
            this.showToast(error.message, 'error');
            throw error;
        }
    },

    setUser(user) {
        this.state.user = user;
        if(user) {
            localStorage.setItem('quiz_user', JSON.stringify(user));
        } else {
            localStorage.removeItem('quiz_user');
        }
        this.updateNav();
    },

    logout() {
        this.setUser(null);
        window.location.href = 'index.html';
    },

    updateNav() {
        const links = document.getElementById('nav-links');
        const auth = document.getElementById('auth-buttons');
        
        if(!links || !auth) return;

        if (this.state.user) {
            if(this.state.user.role === 'admin') {
                links.innerHTML = `
                    <a href="admin.html">Dashboard</a>
                    <a href="#" onclick="alert('Manage Students')">Students</a>
                    <a href="#" onclick="alert('Manage Quizzes')">Quizzes</a>
                `;
            } else {
                links.innerHTML = `
                    <a href="dashboard.html">My Dashboard</a>
                    <a href="result.html">My Results</a>
                `;
            }
            
            auth.innerHTML = `
                <span style="margin-right: 15px; font-weight: 600;">Hi, ${this.state.user.full_name.split(' ')[0]}</span>
                <button class="btn btn-outline" onclick="App.logout()">Logout</button>
            `;
        } else {
            links.innerHTML = `
                <a href="index.html">Home</a>
            `;
            auth.innerHTML = `
                <button class="btn btn-outline" onclick="window.location.href='login.html'">Login</button>
                <button class="btn btn-primary" onclick="window.location.href='register.html'">Register</button>
            `;
        }
    },

    showToast(msg, type = 'success') {
        let toast = document.getElementById('toast');
        if(!toast) {
            toast = document.createElement('div');
            toast.id = 'toast';
            document.body.appendChild(toast);
        }
        toast.className = `toast toast-${type} show`;
        toast.textContent = msg;
        setTimeout(() => toast.className = `toast toast-${type}`, 3000);
    }
};

document.addEventListener('DOMContentLoaded', () => {
    App.updateNav();
});
