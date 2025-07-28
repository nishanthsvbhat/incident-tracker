const form = document.getElementById("incident-form");
const titleInput = document.getElementById("title");
const descriptionInput = document.getElementById("description");
const incidentList = document.getElementById("incident-list");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const title = titleInput.value.trim();
  const description = descriptionInput.value.trim();

  if (!title || !description) return;

  const response = await fetch("http://localhost:5000/api/incidents", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title, description }),
  });

  const data = await response.json();
  if (data.status === "logged") {
    titleInput.value = "";
    descriptionInput.value = "";
    fetchIncidents();
  }
});

async function fetchIncidents() {
  const res = await fetch("http://localhost:5000/api/incidents");
  const incidents = await res.json();

  incidentList.innerHTML = "";
  incidents.forEach(({ title, description }) => {
    const li = document.createElement("li");
    li.innerHTML = `<strong>${title}</strong><br>${description}`;
    incidentList.appendChild(li);
  });
}

fetchIncidents(); // load on page start
