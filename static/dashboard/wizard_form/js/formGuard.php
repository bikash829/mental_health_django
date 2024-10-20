<script>
    let ageGuard = document.getElementById('user_dob');
    let currentDate = new Date();

    let currentDay, currentMonth, currentYear;
    currentDay = currentDate.getDay() < 10 ? `0${currentDate.getDay()}` : currentDate.getDay();
    currentMonth = currentDate.getMonth() < 10 ? `0${currentDate.getMonth()}` : currentDate.getMonth();
    currentYear = currentDate.getFullYear();

    let minYear = `${currentYear-10}-${currentMonth}-${currentDay}`;

    ageGuard.max = minYear;
</script>