const API_URL = 'http://127.0.0.1:8000';

const App = {
    state: {
        user: JSON.parse(localStorage.getItem('chat_user')) || null,
        activeChat: null
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
            console.error(error);
            throw error;
        }
    },

    setUser(user) {
        this.state.user = user;
        if(user) {
            localStorage.setItem('chat_user', JSON.stringify(user));
        } else {
            localStorage.removeItem('chat_user');
        }
    },

    logout() {
        this.setUser(null);
        window.location.href = 'index.html';
    }
};
