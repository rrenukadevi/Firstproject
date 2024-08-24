$(document).ready(function() {
   $('#addTask').click(function() {
      var task = $('#TaskInput').val();
      if (task) {
       // Append list item to the list
       $('#taskList').append('<li> <span class="TaskText">'+ task + '</span><span class="editButton">Edit</span><span class="removeButton">Remove</span></li>');
       $('#TaskInput').val('');
      }
   });

   // Highlight input field on focus 
   $('#TaskInput').focus(function() {
       $(this).addClass('highlight');
   });

   // Remove highlight from input on blur
   $('#TaskInput').blur(function() {
       $(this).removeClass('highlight');
   });

   // Mark task as completed 
   $('#taskList').on('click', '.TaskText', function () {
       $(this).toggleClass('completed');
   });
   // remove task from the list
   $('#taskList').on('click','.removeButton',function() {
      $(this).parent().remove();
   })
   
   // Edit task list 
   $('#taskList').on('click','.editButton',function() {
    var $TaskText= $(this).siblings('.TaskText')
    var currentText = $TaskText.text()
    var newText = prompt('Edit Task:' , currentText)
    if(newText) {
      $TaskText.text(newText)
    }
   })

   //Event for mouseenter
    $('#taskList').on('mouseenter','.TaskText' , function() {
      $(this).css('cursor','pointer')
    })
});
