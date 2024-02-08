$('#deleteModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Button that triggered the modal
    var pk = button.data('pk'); // Extract info from data-* attributes
    var modal = $(this);
    modal.find('#deleteForm').attr('action', pk );
});



//action("{% url 'delete_view' " + pk + " %}")
