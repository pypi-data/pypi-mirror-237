import React, { useContext } from "react";
import Overridable from "react-overridable";
import { PropTypes } from "prop-types";
import { Grid } from "semantic-ui-react";
import { LayoutSwitcher } from "react-searchkit";
import { ResultCountWithState } from "./ResultCount";
import { i18next } from "@translations/oarepo_ui/i18next";
import { SearchConfigurationContext } from "@js/invenio_search_ui/components";
import { SearchAppSort } from "./SearchAppSort";

export const SearchAppResultOptions = ({ sortOptions, layoutOptions }) => {
  const { buildUID } = useContext(SearchConfigurationContext);
  const multipleLayouts =
    Object.values(layoutOptions).filter((i) => i).length > 1;
  return (
    <Grid>
      <Grid.Row verticalAlign="middle">
        <Grid.Column floated="left" textAlign="left" width={5}>
          <ResultCountWithState />
        </Grid.Column>
        <Grid.Column textAlign="right" floated="right" width={8}>
          {sortOptions && (
            <Overridable id={buildUID("SearchApp.sort")} options={sortOptions}>
              <SearchAppSort />
            </Overridable>
          )}
        </Grid.Column>
        {multipleLayouts ? (
          <Grid.Column width={3} textAlign="right">
            {multipleLayouts && <LayoutSwitcher />}
          </Grid.Column>
        ) : null}
      </Grid.Row>
    </Grid>
  );
};

SearchAppResultOptions.propTypes = {
  currentResultsState: PropTypes.object.isRequired,
  sortOptions: PropTypes.arrayOf(
    PropTypes.shape({
      sortBy: PropTypes.string,
      text: PropTypes.string,
    })
  ),
  paginationOptions: PropTypes.shape({
    defaultValue: PropTypes.number,
    resultsPerPage: PropTypes.array,
  }),
  layoutOptions: PropTypes.object,
};
