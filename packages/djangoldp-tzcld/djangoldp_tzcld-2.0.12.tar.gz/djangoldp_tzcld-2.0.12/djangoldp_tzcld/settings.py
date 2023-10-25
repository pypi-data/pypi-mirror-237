COMMUNITY_NESTED_FIELDS = ['tzcld_profile', 'tzcld_profile_identity', 'tzcld_community_synthesis_followed', 'tzcld_community_requests']
COMMUNITY_ADMIN_INLINES = [("djangoldp_tzcld.admin", "TzcldCommunityInline",)]
USER_NESTED_FIELDS = ['tzcld_profile']