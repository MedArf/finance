// frontend/components/main_dashboard.js
class MainDashboard extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
    }

    connectedCallback() {
        this.shadowRoot.innerHTML = `
            <accounting-aggregator></accounting-aggregator>
            <div class="entries">
                <accounting-entry
                    type="income"
                    label="Monthly Salary"
                    amount="3500"
                    category="Income"
                    subcategory="Salary"
                    counterparty="Tech Corp Inc"
                    date="2023-11-01">
                </accounting-entry>

                <accounting-entry
                    type="expense"
                    label="Office Rent"
                    amount="1200"
                    category="Housing"
                    subcategory="Rent"
                    counterparty="Prime Properties"
                    date="2023-11-01">
                </accounting-entry>

                <accounting-entry
                    type="expense"
                    label="Groceries"
                    amount="450"
                    category="Food"
                    counterparty="Supermarket"
                    date="2023-11-02">
                </accounting-entry>
            </div>
        `;
    }
}

customElements.define('main-dashboard', MainDashboard);
