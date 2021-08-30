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
    backdrop: "rgba(0,0,0,0.95)",
    timer: 2000,
    showConfirmButton: false,
  });
};

const addCreditsSuccess = (result) => {
  Swal.fire({
    icon: "success",
    title: "You are Rock!",
    text: `You get $${result}!`,
    backdrop: "rgba(0,0,0,0.95)",
    timer: 2000,
    showConfirmButton: false,
  });
};

const noUserLogin = (url) => {
  Swal.fire({
    icon: "warning",
    title: "Oops...",
    text: "To continue you must login",
    backdrop: "rgba(0,0,0,0.95)",
    timer: 4000,
    footer: `<a href="${url}" class="text-secondary">Sign In</a>`,
    showConfirmButton: false,
  });
};

const notCreditsEnough = (url) => {
  Swal.fire({
    icon: "error",
    title: "Oh no!",
    text: "Insufficient credits",
    backdrop: "rgba(0,0,0,0.95)",
    timer: 4000,
    footer: `<a href="${url}" class="text-secondary">Buy credits</a>`,
    showConfirmButton: false,
  });
};

const stockEmpty = () => {
  Swal.fire({
    icon: "warning",
    title: "Oh no!",
    text: "The stock is empty",
    backdrop: "rgba(0,0,0,0.95)",
    timer: 4000,
    showConfirmButton: false,
  });
};

const productNoEnough = (num) => {
  Swal.fire({
    icon: "info",
    title: "Wait!",
    text: `Only left ${num} vape in the stock`,
    backdrop: "rgba(0,0,0,0.95)",
    timer: 4000,
    showConfirmButton: false,
  });
};

const quantityError = () => {
  Swal.fire({
    icon: "question",
    title: "What?",
    text: "Please, buy me a vape",
    backdrop: "rgba(0,0,0,0.95)",
    timer: 4000,
    showConfirmButton: false,
  });
};
