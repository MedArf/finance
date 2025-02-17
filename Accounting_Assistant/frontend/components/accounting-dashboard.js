class AccountingDashboard extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: "open" });
        this.state = { entries: [] };
    }

    connectedCallback() {
        this.render();
        this.fetchEntries();
    }

    async fetchEntries() {
        try {
            //TODO: get user id from cookie
            const userId = 1
            const response = await fetch("/api/entries?user_id=" + userId);
            this.state.entries = await response.json();

            this.renderEntries();
        } catch (error) {
            console.error("Error fetching entries:", error);
        }
    }

    render() {
        this.shadowRoot.innerHTML = `
            <link rel="stylesheet" href="style.css">
						<custom-sidebar></custom-sidebar>
            <div class="accounting-dashboard">
                <div class="dashboard-tabs">
                    <span class="dashboard-tab active" data-view="list">List View</span>
                    <span class="dashboard-tab" data-view="balance">Balance Sheet</span>
                </div>
                <div class="dashboard-content">
                    <div id="list-view" class="view active"></div>
                    <div id="balance-sheet" class="view">
                        <div class="balance-column income-column"><h3>Income</h3></div>
                        <div class="balance-column expense-column"><h3>Expenses</h3></div>
                    </div>
                </div>
            </div>
        `;

        // Tab Switching
        this.shadowRoot.querySelectorAll(".dashboard-tab").forEach(tab => {
            tab.addEventListener("click", () => {
                this.shadowRoot.querySelectorAll(".dashboard-tab").forEach(t => t.classList.remove("active"));
                tab.classList.add("active");

                const view = tab.dataset.view;
                this.shadowRoot.querySelectorAll(".view").forEach(v => v.classList.remove("active"));
                this.shadowRoot.querySelector(`#${view}-view`)?.classList.add("active");
            });
        });
    }

    renderEntries() {
        const listView = this.shadowRoot.querySelector("#list-view");
        const incomeColumn = this.shadowRoot.querySelector(".income-column");
        const expenseColumn = this.shadowRoot.querySelector(".expense-column");

        listView.innerHTML = "";
        incomeColumn.innerHTML = "<h3>Income</h3>";
        expenseColumn.innerHTML = "<h3>Expenses</h3>";

        this.state.entries.forEach(entry => {
            const entryElement = document.createElement("accounting-entry");
            entryElement.setAttribute("reference", entry.reference);
            entryElement.setAttribute("amount", entry.amount);
            entryElement.setAttribute("category", entry.category);
            entryElement.setAttribute("subcategory", entry.subcategory);
            entryElement.setAttribute("from", entry.from);
            entryElement.setAttribute("to", entry.to);

            listView.appendChild(entryElement);

            if (parseFloat(entry.amount) >= 0) {
                incomeColumn.appendChild(entryElement.cloneNode(true));
            } else {
                expenseColumn.appendChild(entryElement.cloneNode(true));
            }
        });
    }
}

customElements.define("accounting-dashboard", AccountingDashboard);
