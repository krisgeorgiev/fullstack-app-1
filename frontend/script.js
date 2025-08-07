document.getElementById('messageForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const message = document.getElementById('message').value;

  try {
    const response = await fetch('http://localhost:8000/message', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ message })
    });

    const data = await response.json();
    alert(`Server says: ${data.reply}`);
  } catch (error) {
    console.error('Error:', error);
  }
});
