//    2) Crie uma classe com o nome de meunome em CSS (externo) e faça as configurações...
document.getElementById("res2").innerHTML =
	"<p class='meunome'>Caio Tsuyoshi Hayashi</p>";

//    3) Faça um script que leia um número inteiro, em seguida calcule e mostre o dobro desse número.
document.getElementById("double").addEventListener("submit", (e) => {
	e.preventDefault();

	const value = e.target.children[0].value;
	const double = value * 2;

	document.getElementById("res3").innerText = double;
});

//    4) Faça um script para somar dois números informados pelo usuário.
document.getElementById("sum").addEventListener("submit", (e) => {
	e.preventDefault();

	const num1 = parseFloat(e.target.children[0].value);
	const num2 = parseFloat(e.target.children[1].value);

	const sum = num1 + num2;

	document.getElementById("res4").innerText = sum;
});

//    5) Faça um script para calcular o quadrado de um número informado pelo usuário.
document.getElementById("sqrt").addEventListener("submit", (e) => {
	e.preventDefault();

	const input = parseFloat(e.target.children[0].value);

	const sqrt = input ** 2;

	document.getElementById("res5").innerText = sqrt;
});

//    6) Faça um script que leia três notas reais, calcule e mostre a média dessas notas.
document.getElementById("avarage").addEventListener("submit", (e) => {
	e.preventDefault();

	const note1 = parseFloat(e.target.children[0].value);
	const note2 = parseFloat(e.target.children[1].value);
	const note3 = parseFloat(e.target.children[2].value);

	const avarage = (note1 + note2 + note3) / 3;

	document.getElementById("res6").innerText = avarage;
});

//    7) Faça um programa que receba três números inteiros, calcule e mostre a soma desses números.
document.getElementById("sumThree").addEventListener("submit", (e) => {
	e.preventDefault();

	const num1 = parseFloat(e.target.children[0].value);
	const num2 = parseFloat(e.target.children[1].value);
	const num3 = parseFloat(e.target.children[2].value);

	const sum = num1 + num2 + num3;

	document.getElementById("res7").innerText = sum;
});

//    8) Faça um script para calcular e mostrar a área de um triângulo (área = (base * altura) /2.
document.getElementById("triangle").addEventListener("submit", (e) => {
	e.preventDefault();

	const base = parseFloat(e.target.children[0].value);
	const height = parseFloat(e.target.children[1].value);

	const area = (base * height) / 2;

	document.getElementById("res8").innerText = area;
});

//    9) Faça um script que leia o nome de uma pessoa, o ano de nascimento dessa pessoa e o ano atual, calcule e mostre a idade dessa pessoa e seu nome em linhas separadas.
document.getElementById("show").addEventListener("submit", (e) => {
	e.preventDefault();

	const name = e.target.children[0].value;
	const yearOfBirth = parseFloat(e.target.children[1].value);
	const currYear = parseFloat(e.target.children[2].value);

	const age = currYear - yearOfBirth;

	document.getElementById("res9").innerHTML = `
        <p>Nome: ${name}</p>
        <p>Idade: ${age}</p>
    `;
});

//    10) Faça um script que receba a altura de um degrau de uma escada e a altura que um pedreiro deseja alcançar utilizando essa escada, calcule e mostre quantos degraus ele deverá subir para atingir seu objetivo, os valores fornecidos devem ser em metros.
document.getElementById("ladder").addEventListener("submit", (e) => {
	e.preventDefault();

	const step = parseFloat(e.target.children[0].value);
	const totalLadder = parseFloat(e.target.children[1].value);

	const qtyStep = totalLadder/step;

	document.getElementById("res10").innerText = qtyStep
});

