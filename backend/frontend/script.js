// script.js

const API_BASE_URL = "https://incident-tracker-8jmd.onrender.com";

// Function to log a new incident
async function logIncident() {
  const description = document.getElementById("incident-description").value;
  const severity = document.getElementById("incident-severity").value;

  if (!description || !severity) {
    alert("Please enter both description and severity.");
    return;
  }

  const incidentData = {
    description: description,
    severity: severity,
    timestamp: new Date().toISOString()
  };

  try {
    const response = await fetch(`${API_BASE_URL}/incident`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(incidentData)
    });

    const result = await response.json();

    if (response.ok) {
      alert("✅ Incident logged successfully!");
      document.getElementById("incident-description").value = "";
      document.getElementById("incident-severity").value = "low";
      fetchIncidents(); // Refresh list
    } else {
      alert("❌ Failed to log incident: " + result.error);
    }
  } catch (err) {
    console.error("Error logging incident:", err);
    alert("⚠️ Network error. Please try again.");
  }
}

// Function to fetch and display all incidents
async function fetchIncidents() {
  try {
    const response = await fetch(`${API_BASE_URL}/incidents`);
    const incidents = await response.json();

    const incidentList = document.getElementById("incident-list");
    incidentList.innerHTML = "";

    incidents.forEach((incident) => {
      const listItem = document.createElement("li");
      listItem.textContent = `${incident.timestamp} | ${incident.severity.toUpperCase()}: ${incident.description}`;
      incidentList.appendChild(listItem);
    });
  } catch (err) {
    console.error("Error fetching incidents:", err);
    alert("⚠️ Could not fetch incident list.");
  }
}

// Call fetchIncidents on page load
window.onload = fetchIncidents;
