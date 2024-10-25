const classifyText = () => {
    const text = document.getElementById('text_Input').value;

    console.log(text)
    axios.post('http://192.168.109.38:8080/predict',
        { content: text },
        {
            headers: {
                'Content-Type': 'application/json'
            }
        }
    )
        .then(response => {
            console.log(response)
            prediction = response.data.prediction
            console.log(prediction)

            document.getElementById('prediction').textContent = `Prediction: ${prediction}`
        })
}