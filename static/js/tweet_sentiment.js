const classifyText = () => {
    const text = document.getElementById('text_Input').value;

    console.log(text);
    axios.post('https://tweet-sentiment-analysis-web-app-o19j.onrender.com//predict',
        { content: text },
        {
            headers: {
                'Content-Type': 'application/json'
            }
        }
    )
        .then(response => {
            console.log(response);
            const prediction = response.data.prediction;
            console.log(prediction);

            const predictionElement = document.getElementById('prediction');
            predictionElement.textContent = `Prediction: ${prediction}`;
            predictionElement.classList.add('show');
        })
        .catch(error => {
            console.error(error);
            const predictionElement = document.getElementById('prediction');
            predictionElement.textContent = 'Error: Unable to classify the text.';
            predictionElement.classList.add('show');
        });
};
