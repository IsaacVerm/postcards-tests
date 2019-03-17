describe('hello', function() {
  it('gives me my personalized credentials', function() {
    cy.visit(`${Cypress.env('baseUrl')}/credentials/view/Isaac`);
    cy.get('body > p')
      .should('contain', 'credentials')
      .should('contain', 'Isaac');
  });
});
