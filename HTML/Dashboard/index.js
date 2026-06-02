function openModal(buttonID, modalID) {
  const button = document.getElementById(buttonID);
  const modal = document.getElementById(modalID);
  const closeBtn = modal.querySelector(".close")

  button.addEventListener("click", () => {
    modal.style.display = "block";

    // X button
    closeBtn.addEventListener("click", () => {
        modal.style.display = "none";
    });

    // Outside click
    modal.addEventListener("click", (event) => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
  });

}
document.querySelectorAll(".modal").forEach(modal => {
    // X button
    modal.querySelector(".close").addEventListener("click", () => {
        modal.style.display = "none";
    });

    // Outside click
    modal.addEventListener("click", event => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});

openModal("btnHelp","modalHelp");
openModal("btnSettings","modalSettings");