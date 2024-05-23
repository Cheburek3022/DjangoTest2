//let a = Number(prompt("Enter first number"));
//let b = Number(prompt("Enter second number"));
//c = a+b;
//d = a-b;
//e = a*b
//f = a/b
//console.log(c, d, e, f);
//let name = prompt("Enter your name");
//let answer = `Hello, ${name}! How are you?`;
//console.log(answer);
//let a = Number(prompt("Enter first number"));
//let b = Number(prompt("Enter second number"));
//let c = prompt("Enter action you want to do")

//if (c == "+"){
//    console.log(a+b);
//}
//else if(c == "-"){
//   console.log(a-b);
//}
//else if(c == "*"){
//    console.log(a*b);
//}
//else if (c == "/"){
//    console.log(a/b);
//}
//d = c == "+"? a+b : c == "-"? a-b : c == "*"? a*b: c == "/"? a/b: null
//console.log(d);

//let year=prompt("Чи є цей рік високосним?");
//if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
//    console.log(year + " є високосним роком.");
//} else {
//    console.log(year + " не є високосним роком.");
//}

//let a = 0, b=0
//while (a<=10){
//    b += a
//   a++;
//}
//console.log(b)
//let s=0
//for(let i=0; i<0; i++){
//   if (i%2 !=0){
//   continue
//   }
//   s+= 1
//   }

//for (int number = 0; number <= 100; number++) {
//            if (number % 3 == 0) {
//                sum += number;
//                count++;
//            }
//        }
//
//        double average = (double) sum / count;
//        console.log("Середнє арифметичне чисел від 0 до 100, кратних 3: " + average);
//    }
//}
//let sum = 0;
//let a = [1,2,3,4,5,6,7,8,9,10];
//for (let i of a){
//     sum+= i;
//}
//    sum/=a.length
//    console.log(sum)
//let a;
//let sum = 0
//let b = [];
//while (a != "Stop"){
//   d = Number(prompt("Enter the number to add into the massive"))
//   a = prompt("Enter the number to add into the massive, say Stop to stop");
//   b.push(d)
//   }
//for (let i of b){
//       sum += i;
//}
//console.log(sum)

//var a = [10,12,43,21,54,2,132], stop = 0;
//
//while (true){
//    for (let i = 0; 1 < a.length -1; i++){
//        if (a[i]> a[i+1]){
//              temp = a[i];
//              a[1] = a[i+1];
//              a[i+1] = temp;
//              stop++;
//        }
//    }
//    if (! stop){ break }
//}

//var minCity=""
//var maxCity=""
//var min = Infinity
//var max = -Infinity
//let a = {Kiev: 24, Berlin: 13, Washington: 25}
//for (let i in a){
//    if (a[i] > max){
//    max = a[i];
//    maxCity = i
//    }
//    if (a[i] < min){
//    min = a[i];
//    minCity = i
//    }
//}
//console.log(`"Найбільша:" ${max}, ${maxCity}`);
//console.log(`"Найменша:" ${min}, ${minCity}` );

//let users = {};
//
//   let username = prompt("Ім'я:");
//    users[username] = prompt("Пароль:");
//    username = prompt("Ім'я:");
//    let password = prompt("Пароль:");
//    if (users[username] === password) {
//        console.log("Ви успішно увійшли!");
//    }
//    else {
//        console.log("Неправильне ім'я користувача або пароль.");
//    }


//function a(num1,num2, operator){
//     if (operator=="max") {
//         return num1>num2 ? num1:num2;
//     } else if (operator=="min") {
//         return num1<num2 ? num1:num2;
//     }
//}
//console.log(a(3,2, "max"))

//function b(num1, num2, operator){
//     if (operator=="sum") {
//         return num1+num2;
//     } else if (operator=="min"){
//         return num1<num2 ? num1:num2;
//     } else if (operator=="arif"){
//         total=num1+num2
//         mean = total/2;
//     } else if (operator=="max"){
//         return num1>num2 ? num1:num2;
//     }
//}
//console.log(b(3,2, "max"))