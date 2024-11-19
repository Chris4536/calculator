//calc

const display = document.getElementById("display");

function appendToDisplay(input){
    display.value += input;
}

function clearDisplay(){
    display.value = "";
}

function calculate() {
    try {
        // Prevent evaluating "Error"
        if (display.value.trim() === "" || display.value === "Error") {
            display.value = "Error";
            return;
        }

        // Safely evaluate the expression
        display.value = eval(display.value);
    } catch (error) {
        // Handle invalid input or other errors
        display.value = "Error";
    }
}
