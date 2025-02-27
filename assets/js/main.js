/* assets/js/main.js */

// Wait until DOM is ready
document.addEventListener('DOMContentLoaded', function() {
  
    // Student: Major Selection Assistant - show modal on button click
    const suggestMajorBtn = document.getElementById('suggestMajorBtn');
    if (suggestMajorBtn) {
      suggestMajorBtn.addEventListener('click', function() {
        // In a real app, logic would be added to analyze inputs.
        const majorModal = new bootstrap.Modal(document.getElementById('majorModal'));
        majorModal.show();
      });
    }
    
    // Student: Generate Study Plan - display study plan (simulation)
    const generatePlanBtn = document.getElementById('generatePlanBtn');
    if (generatePlanBtn) {
      generatePlanBtn.addEventListener('click', function() {
        const studyPlanContent = document.getElementById('studyPlanContent');
        studyPlanContent.style.display = 'block';
        // Optionally simulate data fetch here
      });
    }
    
    // Student: Suggest Semester Schedule - simulate schedule generation
    const suggestScheduleBtn = document.getElementById('suggestScheduleBtn');
    if (suggestScheduleBtn) {
      suggestScheduleBtn.addEventListener('click', function() {
        alert('Semester schedule has been auto-populated!');
        // Simulation: In a real app, update scheduleContent dynamically.
      });
    }
    
    // Student: Financial Aid Assistant - check eligibility
    const checkAidBtn = document.getElementById('checkAidBtn');
    if (checkAidBtn) {
      checkAidBtn.addEventListener('click', function() {
        const aidModal = new bootstrap.Modal(document.getElementById('aidModal'));
        aidModal.show();
      });
    }
    
    // Student: AI Chat functionality
    const sendChatBtn = document.getElementById('sendChatBtn');
    if (sendChatBtn) {
      sendChatBtn.addEventListener('click', function() {
        const chatInput = document.getElementById('chatInput');
        const chatMessages = document.getElementById('chatMessages');
        if (chatInput.value.trim() !== "") {
          // Append student message
          const userMsg = document.createElement('p');
          userMsg.innerHTML = `<strong>You:</strong> ${chatInput.value}`;
          chatMessages.appendChild(userMsg);
          // Simulate AI response
          const aiMsg = document.createElement('p');
          aiMsg.innerHTML = `<strong>AI:</strong> That's interesting! Let's explore that further.`;
          chatMessages.appendChild(aiMsg);
          chatInput.value = "";
          chatMessages.scrollTop = chatMessages.scrollHeight;
        }
      });
    }
    
    // Admin: Save new course functionality
    const saveCourseBtn = document.getElementById('saveCourseBtn');
    if (saveCourseBtn) {
      saveCourseBtn.addEventListener('click', function() {
        // Simulation: Save course form data
        alert('New course has been added successfully!');
        // Optionally, update the DOM to reflect new course addition
      });
    }
    
    // Financial Aid: Check Scholarship Eligibility (simulation)
    const checkScholarshipBtn = document.getElementById('checkScholarshipBtn');
    if (checkScholarshipBtn) {
      checkScholarshipBtn.addEventListener('click', function() {
        const scholarshipResults = document.getElementById('scholarshipResults');
        scholarshipResults.style.display = 'block';
        // In real app, perform logic to check eligibility
      });
    }
    
  });
  