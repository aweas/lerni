<p>
Search: <input id="filter" type="text">
<select id="competition_group_select">
  <option value="gimnazjum_olimpiady">Gimnazjum Olimpiady</option>
  <option value="gimnazjum_konkursy">Gimnazjum Konkursy</option>
  <option value="liceum_olimpiady">Liceum Olimpiady</option>
  <option value="liceum_konkursy">Liceum Konkursy</option>
</select>
</p>
<div id="jtable"></div>
<script>
head.js(jquery, jquery_ui, jtable, jtable_pl, function(){
        $('#jtable').jtable({
            title: "Olimpijczycy - Gimnazjum",
            paging: true,
            pageSize: 10,
            selecting: true,
            sorting: true,
            defaultSorting: 'id DESC',
        actions: {
            listAction: '/api?format=jsonp&method=lerni.competitors.getList'
        },
        fields: {
            id: {
                    key: true,
                    list: false,
            },
            first_name: {
                    title: 'Imię',
                    width: '10%'
            },
            last_name: {
                    title: 'Nazwisko',
                    width: '10%'
            },
            competition_id: {
                    title: 'Nazwa konkursu/olimpiady',
                    options: '/api?format=jsonp&method=lerni.competitors.competitions.nameList',
                    width: '30%'
            },
            competitor_type_id: {
                    title: 'Stopień',
                    options: '/api?format=jsonp&method=lerni.competitors.types.nameList',
                    width: '10%'
            },
            subject_id: {
                    title: 'Przedmiot',
                    options: '/api?format=jsonp&method=lerni.subjects.nameList',
                    width: '10%'
            },
            competitor_tutor_id: {
                    title: 'Opiekun',
                    options: '/api?format=jsonp&method=lerni.competitors.tutors.nameList',
                    width: '20%'
            },
            year: {
                    title: 'Rok szkolny',
                    width: '10%'
            },
        }
    });
    var search_competitors = function(){
            $('#jtable').jtable('load', {
                name: $("#filter").val(),
                competitionGroupId: $("#competition_group_select option:selected").val()
            });
            var a = {"gimnazjum_olimpiady":"Olimpijczycy - Gimnazjum", "gimnazjum_konkursy":"Konkursowicze - Gimnazjum",
                     "liceum_olimpiady":"Olimpijczycy - Liceum", "liceum_konkursy":"Konkursowicze - Liceum"};
            $('#jtable .jtable-title-text').html(a[$("#competition_group_select option:selected").val()])
    }
    $("#competition_group_select").change(search_competitors);
    $("#filter").on('input', search_competitors);
    search_competitors();
});
</script>