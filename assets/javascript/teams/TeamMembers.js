'use strict';
import React from "react";
import {getMembershipUrl} from "./urls";


const TeamMemberTableRow = function(props) {

  const getMemberDisplay = function() {
    // admins can edit anyone. non-admins can edit themselves.
    if (props.team?.is_admin || props.user_id === props.actingUser.id) {
      const membershipUrl = getMembershipUrl(
        props.apiUrls['single_team:team_membership_details'],
        props.team.slug,
        props.id,
      );
      return <a href={membershipUrl}>{props.display_name}</a>
    } else {
      return props.display_name;
    }
  }

  return (
    <tr>
      <td>
        {getMemberDisplay()}
      </td>
      <td>{props.role}</td>
    </tr>
  );
};

export const TeamMemberList = function (props) {
  return (
    <section className="app-card">
      <h3 className="pg-subtitle">Team Members</h3>
      <div className='table-responsive'>
        <table className="table is-striped is-fullwidth">
          <thead>
          <tr>
            <th>Member</th>
            <th>Role</th>
          </tr>
          </thead>
          <tbody>
          {
            props.members.map((membership, index) => {
              return <TeamMemberTableRow key={membership.id} index={index} apiUrls={props.apiUrls} team={props.team} actingUser={props.user} {...membership} />;
            })
          }
          </tbody>
        </table>
      </div>
    </section>
  );
};
