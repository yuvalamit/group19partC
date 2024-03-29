window.onload = function () {
  // const buttons = document.querySelectorAll(".categoryBtn");
  //
  // // TODO: להוסיף את הקישור לקטגוריה
  // buttons.forEach((button) => {
  //   button.addEventListener("click", () => {
  //     const category = button.getAttribute("data-category");
  //     window.location.href = "Category.html";
  //   });
  // });
  // loadRecipes();
};

const loadRecipes = () => {
  //console.log(all_recipes);
  const recipes = JSON.stringify(all_recipes);
  // console.log(recipes);
  recipes.forEach((recipe) => {
    createRecipeCube(recipe);
  });
};

const createRecipeCube = (recipe) => {
  const recipeDiv = document.createElement("div");
  recipeDiv.classList.add("recipe");

  const heading = document.createElement("h3");
  heading.textContent = recipe.name;

  const imageLink = document.createElement("a");
  imageLink.href = "Recipe.html";

  const image = document.createElement("img");
  image.src = recipe.image;
  image.alt = recipe.name;
  image.classList.add("recipeImage");

  imageLink.appendChild(image);

  const duration = document.createElement("h4");
  duration.textContent = `${recipe.hardness} | ${recipe.minutes} דקות`;

  recipeDiv.appendChild(heading);
  recipeDiv.appendChild(imageLink);
  recipeDiv.appendChild(duration);

  const allRecipes = document.getElementById("AllRecoRecipes");
  allRecipes.appendChild(recipeDiv);
};