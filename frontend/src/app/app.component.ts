import { Component, OnInit } from '@angular/core';
import { Apollo, gql } from 'apollo-angular';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'API-CRUD-Graphql';

  constructor(private apollo: Apollo) {}

  ngOnInit() {
    this.apollo
      .watchQuery({
        query: gql`
          {
            allStudent{
              name
              age
            }
          }
        `,
      })
      .valueChanges.subscribe(result => {
        console.log(result.data);
      });
  }
}
