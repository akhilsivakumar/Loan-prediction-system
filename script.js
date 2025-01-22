document.getElementById("loanForm").addEventListener("submit", function(event) {
    event.preventDefault();  // Prevent the form from submitting normally

    const creditScore = document.getElementById("credit_score").value;
    const loanAmount = document.getElementById("loan_amount").value;
    const salary = document.getElementById("salary").value;
    const maritalStatus = document.getElementById("marital_status").value;
    const employment = document.getElementById("employment").value;
    const propertyArea = document.getElementById("property_area").value;

    const loanData = {
        credit_score: creditScore,
        loan_amount: loanAmount,
        salary: salary,
        marital_status: maritalStatus,
        employment: employment,
        property_area: propertyArea
    };

    // Make a POST request to your backend to predict loan eligibility
    fetch("http://localhost:5000/predict", {  // Replace with your backend endpoint
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(loanData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("eligibilityResult").textContent = data.prediction;
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
