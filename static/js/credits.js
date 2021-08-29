const purchase_validate = (credits, price) => {
  if ((credits === "") | (credits === "None")) {
    noUserLogin();
  } else if (parseFloat(credits) < parseFloat(price)) {
    notCreditsEnough();
  } else if (parseFloat(credits) > parseFloat(price)) {
    console.log("Comprar");
    // Redirect to 'cart' route
  }
};

const creditsResult = (id, value, result) => {
  if (value === result) {
    result = Math.abs(result);
    addCreditsSuccess(result);
    setTimeout(() => window.location.replace(`${id}/${result}`), 2000);
  } else {
    addCreditsFail();
    setTimeout(() => window.location.reload(), 2000);
  }
};

const addCreditsFail = () => {
  Swal.fire({
    icon: "error",
    title: "Incorrect",
    text: "Come back later",
    backdrop: "rgba(0,0,0,0.85)",
    timer: 2000,
    showConfirmButton: false,
  });
};

const addCreditsSuccess = (result) => {
  Swal.fire({
    icon: "success",
    title: "You are Rock!",
    text: `You get $${result}!`,
    backdrop: "rgba(0,0,0,0.85)",
    timer: 2000,
    showConfirmButton: false,
  });
};

const noUserLogin = () => {
  Swal.fire({
    icon: "warning",
    title: "Oops...",
    text: "To continue you must login",
    backdrop: "rgba(0,0,0,0.85)",
    timer: 4000,
    footer: '<a href="login/" class="text-secondary">Sign In</a>',
    showConfirmButton: false,
  });
};

const notCreditsEnough = () => {
  Swal.fire({
    icon: "error",
    title: "Oh no!",
    text: "You no have money",
    backdrop: "rgba(0,0,0,0.85)",
    timer: 4000,
    footer: '<a href="credits/" class="text-secondary">Buy credits</a>',
    showConfirmButton: false,
  });
};
