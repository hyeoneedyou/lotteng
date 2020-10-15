$(function () {
  // Sidebar toggle behavior
  $('#sidebarCollapseInner').on('click', function () {
    $('#sidebar, #content').toggleClass('active');
  });
  $('#sidebarCollapse').on('click', function () {
    $('#sidebar, #content').toggleClass('active');
  });

});
