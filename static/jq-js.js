$('#deleteModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Button that triggered the modal
    var pk = button.data('pk'); // Extract info from data-* attributes
    var modal = $(this);
    modal.find('#deleteForm').attr('action', pk );
});

$(document).on("select2:open", () => {
  document.querySelector(".select2-container--open .select2-search__field").focus()
})



//action("{% url 'delete_view' " + pk + " %}")
