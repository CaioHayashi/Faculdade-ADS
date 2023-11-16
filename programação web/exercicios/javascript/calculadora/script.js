document.getElementById("form-calc")
    .addEventListener("submit", (e) => {
	e.preventDefault();

	const value1 = document.getElementById("value-1").value;
	const value2 = document.getElementById("value-2").value;
	const result = document.getElementById("res");
	const radioChecked = [...document.getElementsByName("op")].find(
		(input) => input.checked
	).value;

	if (!value1.length || !value2.length) {
		return alert("preencha os campos");
	}

	try {
		result.value = eval(`${value1} ${radioChecked} ${value2}`);
	} catch {
		alert("digite apenas números");
		result.value = "";
	}
});
