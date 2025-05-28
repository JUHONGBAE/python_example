// 비동기 제어
// const user = {};

//     setTimeout(() => {
//         user.name = "weniv";
//     }, 0);

// console.log(user)

// 콜백함수
// const user = {};

// function setUser(callback) {
//     setTimeout(() => {
//         user.name = "weniv";
//         callback(user);
//     }, 0);
// }

//  function printUser(user) {
//      console.log(user);
//  }

// // setUser(printUser);
// // setUser((user) => console.log(user));

// function setUser(callback) {
//     setTimeout(() => {
//         user.name = "weniv";
//         user.age = 20;
//         callback(user)
//     }, 0)
// }

// function roleCheck(user, callback){
//     setTimeout(() => {
//         if (user.age >= 20) {
//             user.role = "성인";
//         }
//         else {
//             user.role = "학생";
//         }
//         callback(user);
//     }, 1000);
// }

// setUser((user) => roleCheck(user, printUser));

// func1(function(result1) {
//     func2(result1, function (result2) {
//         fun3(result2, function (result3) {
//             //계속되는 중첩...
//         });
//     });
// });

// 문제 1
// 피자 주문이 접수되었습니다
// 피자 준비가 완료되었습니다  
// 서울시 강남구로 배달을 시작합니다
// 배달이 완료되었습니다
// 배달 완료!

// function 주문접수(food, user, callback) {
//     setTimeout(() => {
//         console.log(`${food}주문이 접수되었습니다.`)
//         callback()
//     }, 1000);
// }

// function 음식준비(food, callback) {
//     setTimeout(() => {
//         console.log(`${food}준비가 완료되었습니다.`)
//         callback()
//     }, 2000);
// }

// function 배달시작(food, address, callback) {
//     setTimeout(() => {
//         console.log(`${address}로 배달을 시작합니다.`)
//         callback()
//     }, 3000);
// }


// 주문접수("피자", "홍길동", () => {
//     음식준비("피자", () => {
//         배달시작("피자", "서울시 강남구", () => {
//             console.log("배달이 완료되었습니다");
//             console.log("배달 완료!");
//         });
//     });
// });


/* function 주문접수(음식명, callback) {
    console.log(`${음식명} 주문이 접수되었습니다`);
    setTimeout(() => {
        callback(음식명);
    }, 1000);
}

function 음식준비(음식명, callback) {
    console.log(`${음식명} 준비가 완료되었습니다`);
    setTimeout(() => {
        callback();
    }, 2000);
}

function 배달시작(주소, callback) {
    console.log(`${주소}로 배달을 시작합니다`);
    setTimeout(() => {
        console.log("배달이 완료되었습니다");
        callback();
    }, 3000);
}

주문접수("피자", (음식명) => {
    음식준비(음식명, () => {
        배달시작("서울시 강남구", () => {
            console.log("배달 완료!");
        });
    });
}); */
