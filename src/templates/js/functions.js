function drawContributorsGraph(targetTableDataSource, targetCanvas, max) {
        max = typeof max !== 'undefined' ?  max : 20;

        // Get the context of the canvas element we want to select
        var ctx = targetCanvas.getContext("2d");

        var percentageTd = $('.' + targetTableDataSource + ' td');
        var labels = []
                , percentages = [];

        if (percentageTd.length == 0) {
            targetCanvas.style.display = 'none';
            return;
        }

        for (var i = 0; i < percentageTd.length && i < (max * 2) ; i++) {
            var percentageData = percentageTd[i].innerText;
            if (i % 2 == 0) {
                labels.push(percentageData);
            }
            else {
                percentages.push(parseInt(percentageData));
            }
        }
        var data = {
            labels: labels,
            datasets: [
                {
                    label: targetTableDataSource,
                    fillColor: "rgba(220,220,220,0.5)",
                    strokeColor: "rgba(220,220,220,0.8)",
                    highlightFill: "rgba(220,220,220,0.75)",
                    highlightStroke: "rgba(220,220,220,1)",
                    data: percentages
                }
            ]
        };
        new Chart(ctx).Bar(data);
}

function drawContributorStats(targetTableDataSource, targetCanvas, colors) {


        var percentageTd = $('.' + targetTableDataSource + ' td');

        if (percentageTd.length == 0) {
            targetCanvas.style.display = 'none';
            return;
        }

        var data = [];
        for (var i = 0; i < percentageTd.length ; i+=4) {
            var categoryName = percentageTd[i + 1].innerText;

            data.push(
                {
                    value: parseInt(percentageTd[i + 2].innerText),
                    color: colors[categoryName],
                    label: categoryName
                }
            );
        }

        // Get the context of the canvas element we want to select
        var ctx = targetCanvas.getContext("2d");

         new Chart(ctx).Pie(data);
    }



