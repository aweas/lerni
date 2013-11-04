<html xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <title>
                SIS | ${who}: tygodniowy plan lekcji
            </title>
            <link rel="stylesheet" type="text/css" href="/static/sis/base.min.css" />
            <link rel="stylesheet" type="text/css" href="/static/sis/beta.min.css" />
        </head>
        <body>
            <div id="header">
                <h1>
                    <a href="/sis">System Informacyjny Staszica</a> <span class="beta">beta</span>
                </h1>
                <div id="user-tools">
                    Ostatnia aktualizacja planu: ${last_update} |
                        <span>
                            <a href="/login">Zaloguj</a>
                        </span>
                </div>
            </div>
            <div id="menu">
                Menu:
                <ul>
                    <li><a href="/sis">Home</a></li>
                    <!--
                    <li><a href="/now">Now!</a></li>
                    -->
                    <li><a href="/sis/schedule">Plan</a></li>
                    <li><a href="/sis/lucky">Szczęśliwy numerek</a></li>
                    <li><a href="http://www.staszic.edu.pl/zastepstwa/">Zastępstwa</a></li>
                    <li><a href="/sis/about">About</a></li>
                </ul>
            </div>
            <div id="content">
        <h2>${who}: tygodniowy plan lekcji</h2>
        <table border="1">
            <tr>
                <th>lp.</th>
                <th>poniedziałek</th>
                <th>wtorek</th>
                <th>środa</th>
                <th>czwartek</th>
                <th>piątek</th>
            </tr>
            %for x in lessons:
            <tr>
                <td>${x[0]}.</td>
                <td>${"/".join(x[1])}</td>
                <td>${"/".join(x[2])}</td>
                <td>${"/".join(x[3])}</td>
                <td>${"/".join(x[4])}</td>
                <td>${"/".join(x[5])}</td>
            </tr>
            %endfor
        </table>
            </div>
        </body>
</html>