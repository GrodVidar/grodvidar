$('#deleteModal').on('show.bs.modal', function (event) {
    console.log('hejsan');
    var button = $(event.relatedTarget); // Button that triggered the modal
    var pk = button.data('pk'); // Extract info from data-* attributes
    var modal = $(this);
    console.log(modal);
    modal.find('#deleteForm').attr('action', pk );
});

//action("{% url 'delete_view' " + pk + " %}")
