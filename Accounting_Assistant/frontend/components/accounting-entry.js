class AccountingEntry extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: "open" });
    }

    connectedCallback() {
        const reference = this.getAttribute("reference") || "N/A";
        const amount = parseFloat(this.getAttribute("amount") || "0.00");
        const category = this.getAttribute("category") || "General";
        const subcategory = this.getAttribute("subcategory") || "None";
        const from = this.getAttribute("from") || "Unknown";
        const to = this.getAttribute("to") || "Unknown";
        const type = amount >= 0 ? "income" : "expense";

        this.shadowRoot.innerHTML = `
            <link rel="stylesheet" href="static/style.css">
            <div class="entry ${type}">
                <span>${reference}</span>
                <span>$${amount.toFixed(2)}</span>
            </div>
            <div class="properties">
                <button class="property-btn category" data-type="category" data-value="${category}">${category}</button>
                <button class="property-btn subcategory" data-type="subcategory" data-value="${subcategory}">${subcategory}</button>
                <button class="property-btn from" data-type="from" data-value="${from}">From: ${from}</button>
                <button class="property-btn to" data-type="to" data-value="${to}">To: ${to}</button>
            </div>
        `;

        this.shadowRoot.querySelectorAll(".property-btn").forEach(button => {
            button.addEventListener("click", () => {
                const type = button.dataset.type;
                const value = button.dataset.value;

                fetch(`/api/aggregate?${type}=${encodeURIComponent(value)}`)
                    .then(response => response.json())
                    .then(data => console.log(`Aggregated Data for ${type}:`, data))
                    .catch(error => console.error("Error fetching data:", error));
            });
        });
    }
}

customElements.define("accounting-entry", AccountingEntry);
