// const promise = new Promise((resolve, reject) => 
//     {
//         setTimeout(() => {
//         // resolve("요청 성공");
//         reject("요청 실패");
//     }, 1000);
//     });

// promise.then((Response) => {
//     console.log(Response);
// })

// promise.catch((error) => {
//     console.log(error);
// })

// promise
//     .then((response) => {
//         console.log(response);
//     })
//     .catch((error) => {
//         console.log(error);
//     })
//     .finally(() => {
//         console.log("프로미스 종료!");
//     });


// Callback -> Promise 방식으로 수정하기

/* const user = {};

function setUSer(callback) {
    setTimeout(() => {
        user.name = "weniv";
        user.age = 20;
        callback(user);
    }, 0);
}

function printUser(user) {
    console.log(user);
}

function roleCheck(user, callback) {
    setTimeout(() => {
        if (user.age >= 20) {
            user.role = "성인";
        } else {
            user.role = "학생";
        }
        callback(user);
    }, 1000);
}

setUSer((user) => roleCheck(user, printUser)); */



/* const user = {};

function setUser() {
    return new Promise((resolve) => {
        setTimeout(() => {
            user.name = "weniv";
            user.age = 20;
            resolve(user);
        }, 0);
    });
}

function printUser(user) {
    console.log(user);
}

function roleCheck(user) {
    return new Promise((resolve) => {
        setTimeout(() => {
            if (user.age >= 20) {
                user.role = "성인";
            } else {
                user.role = "학생";
            }
            resolve(user);
        }, 1000);
    });
}

setUser()
    .then(user => {
    console.log("성공:", user);
    })
    .catch(error => {
    console.error("실패:", error);
    })
    .finally(() => {
    console.log("프로미스 종료!");
  }); */

const user = {};

function setUser() {
    return new Promise((resolve) => {
        setTimeout(() => {
            user.name = "weniv";
            user.age = 20;
            resolve(user);
        }, 0);
    });
}

function printUser(user) {
    console.log(user);
}

function roleCheck(user) {
    return new Promise((resolve) => {
        setTimeout(() => {
            if (user.age >= 20) {
                user.role = "성인";
            } else {
                user.role = "학생";
            }
            resolve(user);
        }, 0);
    });
}

// setUSer((user) => roleCheck(user, printUser));

// setUser().then((response) => console.log(response));
// setUser()
//     .then(roleCheck)
//     .then((user) => console.log(user));

setUser().then(roleCheck).then(printUser);