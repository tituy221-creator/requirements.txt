<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI वीडियो मेकर</title>
<style>
  body { font-family: sans-serif; background: #0f172a; color: #fff; margin: 0; padding: 20px; text-align: center; }
  h1 { margin-top: 30px; }
  input { width: 90%; max-width: 400px; padding: 14px; font-size: 18px; border-radius: 10px; border: none; margin-top: 20px; }
  button { padding: 14px 28px; font-size: 18px; border: none; border-radius: 10px; background: #22c55e; color: #fff; margin-top: 20px; }
  #status { margin-top: 30px; font-size: 20px; }
  a { color: #38bdf8; font-size: 20px; }
</style>
</head>
<body>
  <h1>🎬 AI वीडियो मेकर</h1>
  <p>विषय लिखें, वीडियो अपने आप बनेगी</p>
  <input id="topic" placeholder="जैसे: अंतरिक्ष के रोचक तथ्य">
  <br>
  <button onclick="start()">वीडियो बनाओ</button>
  <div id="status"></div>
  <div id="link"></div>

<script>
async function start() {
  const topic = document.getElementById('topic').value;
  const s = document.getElementById('status');
  document.getElementById('link').innerHTML = '';
  s.innerText = 'शुरू हो रहा है...';
  const r = await fetch('/create', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({topic})
  });
  const data = await r.json();
  if (data.error) { s.innerText = data.error; return; }
  const id = data.job_id;
  const timer = setInterval(async () => {
    const res = await fetch('/status/' + id);
    const j = await res.json();
    s.innerText = j.status;
    if (j.done) {
      clearInterval(timer);
      if (j.file) {
        document.getElementById('link').innerHTML = '<a href="/download/' + id + '">वीडियो डाउनलोड करें</a>';
      }
    }
  }, 3000);
}
</script>
</body>
</html>
मोबाइल से चलाने के कदम
1.  मोबाइल ब्राउज़र में github.com पर फ्री खाता बनाएँ और एक नई रिपॉज़िटरी बनाएँ।
2.  Add file में Create new file चुनकर ऊपर की तीन फ़ाइलें बनाएँ। index.html का नाम templates/index.html लिखें, तो फ़ोल्डर अपने आप बन जाएगा।
3.  render.com पर गिटहब से लॉगिन करें, New में Web Service चुनें और अपनी रिपॉज़िटरी जोड़ें।
4.  Build Command में pip install -r requirements.txt और Start Command में gunicorn app:app --timeout 600 लिखें।
5.  Environment में दो चाबियाँ जोड़ें: GEMINI_KEY और PEXELS_KEY। ये फ्री में aistudio.google.com और pexels.com/api से मिलती हैं।
6.  Deploy दबाएँ। कुछ मिनट बाद रेंडर आपको एक लिंक देगा, उसे मोबाइल में खोलकर चलाएँ।
