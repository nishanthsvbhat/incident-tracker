const form = document.getElementById("incident-form");
const titleInput = document.getElementById("title");
const descriptionInput = document.getElementById("description");
const incidentList = document.getElementById("incident-list");

// 🔁 Update this to your deployed backend URL
const BASE_URL = "https://incident-tracker-8jmd.onrender.com";

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const title = titleInput.value.trim();
  const description = descriptionInput.value.trim();

  if (!title || !description) return;

  const response = await fetch(`${BASE_URL}/incident`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title, description }),
  });

  const data = await response.json();
  if (data.message === "Incident logged") {
    titleInput.value = "";
    descriptionInput.value = "";
    fetchIncidents();
  }
});

async function fetchIncidents() {
  const res = await fetch(`${BASE_URL}/incidents`);
  const incidents = await res.json();

  incidentList.innerHTML = "";
  incidents.forEach(({ title, description }, index) => {
    const li = document.createElement("li");
    li.innerHTML = `<strong>${index + 1}. ${title}</strong><br>${description}`;
    incidentList.appendChild(li);
  });
}

fetchIncidents(); // load on page start
