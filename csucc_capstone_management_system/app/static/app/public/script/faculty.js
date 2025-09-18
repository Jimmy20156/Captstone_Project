function approveProposal() {
  document.getElementById("review-status").innerHTML = "✅ Proposal Approved!";
  document.getElementById("review-status").style.color = "green";
}

function rejectProposal() {
  document.getElementById("review-status").innerHTML = "❌ Proposal Rejected!";
  document.getElementById("review-status").style.color = "red";
}

function scheduleDefense() {
  const team = document.getElementById("team").value;
  const date = document.getElementById("date").value;
  const status = document.getElementById("schedule-status");

  if (date) {
    status.innerHTML = `📅 Defense scheduled for ${team} on ${date}`;
    status.style.color = "blue";
  } else {
    status.innerHTML = "⚠ Please select a date.";
    status.style.color = "red";
  }
}

function submitGrade() {
  const score = document.getElementById("score").value;
  const comments = document.getElementById("grading-comments").value;
  const status = document.getElementById("grade-status");

  if (score && comments) {
    status.innerHTML = `✅ Grade submitted: ${score}/100 with comments.`;
    status.style.color = "green";
  } else {
    status.innerHTML = "⚠ Please enter score and comments.";
    status.style.color = "red";
  }
}
