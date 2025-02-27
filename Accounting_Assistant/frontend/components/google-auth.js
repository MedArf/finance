class GoogleAuth extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: "open" });
        this.clientId = null; // Store client ID dynamically
    }

    async connectedCallback() {
        await this.fetchClientId();
        this.render();
        this.loadGoogleAPI();
    }

    async fetchClientId() {
        try {
            const response = await fetch("/auth/google/");
            const data = await response.json();
            this.clientId = data.client_id;
    				console.log("Client id", this.clientId);
				} catch (error) {
            console.error("Error fetching Google Client ID:", error);
        }
		}

	render() {
		this.shadowRoot.innerHTML = `
		<link rel="stylesheet" href="/static/style.css">
<button class="gsi-material-button">
  <div class="gsi-material-button-state"></div>
  <div class="gsi-material-button-content-wrapper">
    <div class="gsi-material-button-icon">
      <svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" xmlns:xlink="http://www.w3.org/1999/xlink" style="display: block;">
        <path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"></path>
        <path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"></path>
        <path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"></path>
        <path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"></path>
        <path fill="none" d="M0 0h48v48H0z"></path>
      </svg>
    </div>
    <span class="gsi-material-button-contents">Sign in with Google</span>
    <span style="display: none;">Sign in with Google</span>
  </div>
</button>
<div class="user-info" style="display:none;">
                <img id="user-pic" src="" alt="User">
                <p id="user-name"></p>
                <p id="user-email"></p>
						</div>
`;

				this.shadowRoot.querySelector(".gsi-material-button").addEventListener("click", () => this.signIn());
    }

    loadGoogleAPI() {
        const script = document.createElement("script");
        script.src = "https://accounts.google.com/gsi/client";
        script.onload = () => console.log("Google API Loaded");
        document.body.appendChild(script);
    }

    signIn() {
        if (!this.clientId) {
            console.error("Google Client ID not available.");
            return;
        }

        google.accounts.oauth2.initTokenClient({
            client_id: this.clientId, // Dynamic Client ID
            scope: "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email",
            callback: (response) => this.getUserInfo(response.access_token),
        }).requestAccessToken();
    }

    getUserInfo(token) {
        fetch("https://www.googleapis.com/oauth2/v2/userinfo", {
            headers: { Authorization: `Bearer ${token}` }
        })
        .then(res => res.json())
        .then(user => this.displayUser(user))
        .catch(err => console.error("Error fetching user info:", err));
    }

    displayUser(user) {
 				this.shadowRoot.getElementById("user-pic").src = user.picture;
        this.shadowRoot.getElementById("user-name").textContent = user.name;
        this.shadowRoot.getElementById("user-email").textContent = user.email;
        this.shadowRoot.querySelector(".user-info").style.display = "block";

        // Emit custom event for integration
        this.dispatchEvent(new CustomEvent("user-logged-in", {
            detail: { name: user.name, email: user.email, picture: user.picture },
            bubbles: true,
            composed: true
        }));
    }
}

customElements.define("google-auth", GoogleAuth);

