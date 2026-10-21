# Gemini Enterprise: platform, security, agents, cost, monitoring / A2UI component gallery reference: A2UI component gallery reference to Material catalog navigation components
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 480-506, extracted 2026-10-18

## A2UI component gallery reference

URL: https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/a2ui-component-gallery-reference

This page provides a comprehensive reference for all available A2UI components, including layout, display, interactive, and container components, as well as common properties. 

### Material catalog components and basic catalog components

A2UI provides two distinct component catalogs for building agent user interfaces: the material catalog (#material_catalog_components) and the basic catalog (#basic_catalog_components). 

**Note:** The basic catalog is referred to as the "standard catalog" in v0.8. See the 0.8 component model documentation 

(https://a2ui.org/specification/v0.8-a2ui/#section-2-the-component-model) for information. 

The _material catalog_ contains components specifically designed to adhere to Google Material Design guidelines, offering a richer, more styled set of UI elements that are supported in A2UI v0.9 configurations. 

The _basic catalog_ contains standard, design-system-agnostic UI primitives—such as layouts, actions, and inputs—supported in both A2UI v0.9 and v0.8 configurations. 

### Material catalog components

This section provides a reference for available A2UI Material Design components, including layout, display, navigation, and input components. 

**Note:** The A2UI Material Catalog components are supported in A2UI version v0.9 configurations. For more information about A2UI versions, see Specification Versions 

### Material catalog common properties

All components, regardless of their specific type, share a set of common properties that can be configured: 

|Property|Requir|edDescription|
|---|---|---|
|`id`|Yes|A unique identifier for the component within the current surface.|
|`accessibi`<br>`lity`|No|Attributes to improve accessibility, such as labels and roles.|
|`weight`|No|A value used in`MaterialRow`or`MaterialColumn`layouts to control how<br>much space the component takes up relative to its siblings, similar to<br>`flex-grow`.|

### Material catalog layout components

Layout components are used to structure and arrange other components within the user interface. 

#### MaterialCard

Material Design card container. 

The following table outlines the properties available for the `MaterialCard` component: 

|Property|Requir|ed<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`children`|Yes|-|Defines the children IDs.|
|`appearanc`|`e`No|`raised`|The card appearance style. One of: "outlined", "raised".|

|Property|Requi|red<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`align`|No|`start`|Alignment of children. One of: "center", "end", "start", "stretch".|
|`ariaLabel`|No|-|Discernible text for screen readers. Recommended for<br>accessibility when no visible label is present.|
|`aria`<br>`Labelledby`|No|-|Identifies the element (or elements) that labels the current<br>element. Used for accessibility.|
|`href`|No|-|Optional URL to navigate to when the card is clicked. When set,<br>the card becomes interactive and opens the URL in a new tab.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialCard",
   "appearance": "outlined",
   "children": [
     "card-content"
   ]
 },
 {
   "id": "card-content",
   "component": "MaterialText",
   "text": "Card content"
 }
]
```

#### MaterialColumn

Layout container that arranges items vertically using Material guidelines. 

The following table outlines the properties available for the `MaterialColumn` component: 

|Property|Requir|ed<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`childre`<br>`n`|Yes|-|Defines the children IDs.|
|`justify`|No|`start`|Defines the arrangement of children along the main axis<br>(vertically). One of: "start", "center", "end", "spaceBetween",<br>"spaceAround", "spaceEvenly".|
|`align`|No|`stretch`|Horizontal alignment of children ("start", "center", "end", "stretch").|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialColumn",
   "children": [
     "demo-column-header",
     "demo-column-content",
     "demo-column-footer"
   ],
   "justify": "start",
   "align": "stretch"
 },
 {
   "id": "demo-column-header",
   "component": "MaterialText",
   "text": "Header",
   "usageHint": "h2"
 },
 {
   "id": "demo-column-content",
   "component": "MaterialText",
   "text": "Content goes here",
   "usageHint": "body"
 },
 {
   "id": "demo-column-footer",
   "component": "MaterialText",
   "text": "Footer",
   "usageHint": "caption"
 }
]
```

#### MaterialDialog

Material Design menu dialog container. 

The following table outlines the properties available for the `MaterialDialog` component: 

|Property|Requir|ed<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`open`|No|`false`|Whether the dialog is open. Can be a literal boolean or a data<br>binding reference.|
|`title`|No|-|The title of the dialog.|
|`disable`<br>`Close`|No|`false`|Whether the user can close the dialog by clicking outside or<br>pressing Escape.|
|`width`|No|-|The width of the dialog (e.g. "500px").|
|`height`|No|-|The height of the dialog (e.g. "400px").|
|`children`|Yes|-|Defines the children IDs.|
|`ariaLabel`|No|-|Discernible text for screen readers. Recommended for<br>accessibility when no visible label is present.|
|`aria`<br>`Labelledby`|No|-|Identifies the element (or elements) that labels the current<br>element. Used for accessibility.|
|`aria`<br>`Describedby`|No|-|Identifies the element (or elements) that describes the<br>current element. Used for accessibility.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex<br>container.|

```
[
 {
   "id": "root",
   "component": "MaterialColumn",
   "children": [
     "open-button",
     "confirmation-dialog"
   ],
   "justify": "start",
   "align": "start"
 },
 {
   "id": "open-button",
   "component": "MaterialButton",
   "label": "Delete Item",
   "variant": "raised",
   "action": {
     "event": {
       "name": "requestDelete"
     }
   }
 },
 {
   "id": "confirmation-dialog",
   "component": "MaterialDialog",
   "open": {
     "path": "/app/dialogOpen"
   },
   "title": "Delete Confirmation",
   "children": [
     "dialog-layout"
   ]
 },
 {
   "id": "dialog-layout",
   "component": "MaterialColumn",
   "children": [
     "dialog-text",
     "dialog-actions"
   ],
   "justify": "start",
   "align": "stretch"
 },
 {
   "id": "dialog-text",
   "component": "MaterialText",
   "text": "Are you sure you want to permanently delete this item?"
 },
 {
   "id": "dialog-actions",
   "component": "MaterialRow",
   "children": [
     "cancel-button",
     "confirm-button"
   ],
   "justify": "end",
   "align": "center"
 },
 {
   "id": "cancel-button",
   "component": "MaterialButton",
   "label": "Cancel",
   "variant": "basic",
   "action": {
     "event": {
       "name": "closeDialog"
     }
   }
 },
 {
   "id": "confirm-button",
   "component": "MaterialButton",
   "label": "Delete",
   "variant": "raised",
   "action": {
     "event": {
       "name": "confirmDelete"
     }
   }
 }
]
```

#### MaterialDivider

Material Design dividing line. 

The following table outlines the properties available for the `MaterialDivider` component: 

|Property|Requir|edDefault V|alueDescription|
|---|---|---|---|
|`inset`|No|`false`|Whether the divider is inset.|
|`vertica`|`l`No|`false`|Whether the divider is vertical.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialColumn",
   "children": [
     "text-above",
     "divider",
     "text-below"
   ],
   "justify": "start",
   "align": "stretch"
 },
 {
   "id": "text-above",
   "component": "MaterialText",
   "text": "This is the content above the divider."
 },
 {
   "id": "divider",
   "component": "MaterialDivider",
   "inset": false,
   "vertical": false
 },
 {
   "id": "text-below",
   "component": "MaterialText",
   "text": "This is the content below the divider."
 }
```

#### MaterialExpansionPanel

Material Design expansion panel container. 

The following table outlines the properties available for the `MaterialExpansionPanel` component: 

|Property|Require|d<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`title`|No|-|The title displayed in the expansion panel header.|
|`description`|No|-|The description displayed in the expansion panel header.|
|`expanded`|No|`false`|Whether the panel is expanded. Can be a literal boolean or a<br>data binding reference.|
|`disabled`|No|`false`|Whether the expansion panel is disabled.|
|`ariaLabel`|No|-|Discernible text for screen readers. Recommended for<br>accessibility when no visible label is present.|
|`aria`<br>`Labelledby`|No|-|Identifies the element (or elements) that labels the current<br>element. Used for accessibility.|
|`aria`<br>`Describedby`|No|-|Identifies the element (or elements) that describes the<br>current element. Used for accessibility.|
|`children`|Yes|-|Defines the children IDs.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex<br>container.|

```
[
 {
   "id": "root",
```

- `"component": "MaterialExpansionPanel", "title": "Advanced Options",` 

```
   "description": "Configure advanced settings",
   "expanded": false,
   "children": [
     "panel-content"
   ]
 },
 {
   "id": "panel-content",
   "component": "MaterialText",
   "text": "Advanced settings content goes here"
 }
]
```

#### MaterialGridList

A2UI container component for grid layout. Uses Angular Material Grid List to arrange child components into tiles. 

The following table outlines the properties available for the `MaterialGridList` component: 

|Property|Requir|ed<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`children`|Yes|-|Defines the children IDs.|
|`cols`|No|`2`|Number of columns in the grid list. Can be a literal number or a<br>data binding reference.|
|`row`<br>`Height`|No|`1:1`|Row height ratio or fixed height (e.g. "100px"). Can be a literal<br>string or a data binding reference.|
|`gutter`<br>`Size`|No|`1px`|Size of the grid gutter. Can be a literal string or a data binding<br>reference.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialGridList",
   "cols": 2,
   "rowHeight": "1:1",
   "gutterSize": "8px",
   "children": [
     "card-a",
     "card-b",
     "card-c",
     "card-d"
   ]
 },
 {
   "id": "card-a",
   "component": "MaterialCard",
   "children": [
     "text-a"
   ]
 },
 {
   "id": "text-a",
   "component": "MaterialText",
   "text": "Card A"
 },
 {
   "id": "card-b",
   "component": "MaterialCard",
   "children": [
     "text-b"
   ]
 },
 {
   "id": "text-b",
   "component": "MaterialText",
   "text": "Card B"
 },
 {
   "id": "card-c",
   "component": "MaterialCard",
   "children": [
     "text-c"
   ]
 },
 {
   "id": "text-c",
   "component": "MaterialText",
   "text": "Card C"
 },
 {
   "id": "card-d",
   "component": "MaterialCard",
   "children": [
     "text-d"
   ]
 },
 {
   "id": "text-d",
   "component": "MaterialText",
   "text": "Card D"
 }
]
```

#### MaterialRow

Layout container that arranges items horizontally using Material guidelines. The following table outlines the properties available for the `MaterialRow` component: 

|Property Requir|ed<sup>Default</sup><br>Value|Description|
|---|---|---|
|`childre`<br>Yes|-|Defines the children IDs.|
|`n`|||
|`justify`No|`start`|Defines the arrangement of children along the main axis<br>(horizontally). One of: "start", "center", "end", "spaceAround",<br>"spaceBetween", "spaceEvenly".|
|`align`<br>No|`stretch`|Vertical alignment of children ("start", "center", "end", "stretch").|
|`style`<br>No|-|Inline styles to apply to the element.|
|`weight`<br>No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialRow",
   "children": [
     "item-icon",
     "item-details",
     "item-action"
   ],
   "justify": "spaceBetween",
   "align": "center"
 },
 {
   "id": "item-icon",
   "component": "MaterialIcon",
   "icon": "shopping_bag",
   "color": "primary"
 },
 {
   "id": "item-details",
   "component": "MaterialColumn",
   "children": [
     "item-title",
     "item-subtitle"
   ],
   "justify": "start",
   "align": "start"
 },
 {
   "id": "item-title",
   "component": "MaterialText",
   "text": "Premium Wireless Headphones",
   "usageHint": "subtitle1"
 },
 {
   "id": "item-subtitle",
   "component": "MaterialText",
   "text": "$299.99 \u2022 Active Noise Cancelling",
   "usageHint": "caption"
 },
 {
   "id": "item-action",
   "component": "MaterialButton",
   "label": "Buy Now",
   "variant": "raised",
   "action": {
     "event": {
       "name": "buy_clicked"
     }
   }
 }
]
```

### Material catalog content components

Display and content components are used to present information, media, and status to the user. 

#### MaterialBadge

Displays a Material Design badge over a child element. 

The following table outlines the properties available for the `MaterialBadge` component: 

|Property|Requi|red<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`text`|No|-|Text content to display in the badge.|
|`color`|No|-|Color palette of the badge ("primary", "accent", "warn").|
|`position`|No|`above`<br>`after`|Position of the badge relative to the container ("above after",<br>"above before", "below after", "below before").|
|`size`|No|`medium`|Size of the badge ("small", "medium", "large").|
|`overlap`|No|`true`|Whether the badge should overlap its container.|
|`disabled`|No|`false`|Whether the badge is disabled.|
|`hidden`|No|`false`|Whether the badge is hidden.|

|Property<br>Required<sup>Default</sup><br>Value|Description|
|---|---|
|`descripti`<br>`on`<br>No<br>-|Accessible description for the badge.|
|`children` Yes<br>-|Defines the children IDs.|
|`style`<br>No<br>-|Inline styles to apply to the element.|
|`weight`<br>No<br>-|Layout weight for the element when placed in a flex container.|
|`[`<br>`{`<br>`"id": "root",`<br>`"component": "Materi`<br>`"text": "42",`<br>`"color": "warn",`<br>`"children": [`<br>`"badge-content"`<br>`]`<br>`},`<br>`{`<br>`"id": "badge-content`<br>`"component": "Materi`<br>`"label": "Notificati`<br>`}`<br>`]`|`alBadge",`<br>`",`<br>`alButton",`<br>`ons"`|

#### MaterialIcon

Displays a Material Design icon. 

The following table outlines the properties available for the `MaterialIcon` component: 

PropertyRequiredDefault Value Description `icon` Yes - The name of the Material Icon to display. 

|PropertyRequir|edDefault|Value Description|
|---|---|---|
|`color`<br>No|-|Color palette of the icon (primary, accent, warn).|
|`tooltip`No|-|Optional tooltip text to display on hover/focus.|
|`style`<br>No|-|Inline styles to apply to the element.|
|`weight` No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialIcon",
   "icon": "favorite",
   "color": "warn"
 }
]
```

#### MaterialImage

A2UI component for rendering an image in a Material Design context. Supports rounded corners, aspect ratio, and object-fit properties. 

The following table outlines the properties available for the `MaterialImage` component: 

|Property|Requi|red<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`url`|Yes|-|The URL of the image to display.|
|`alt`|No|-|Accessible alt text for the image.|
|`fit`|No|-|Specifies how the image should be resized to fit its container.<br>One of: "fill", "contain", "cover", "scaleDown", "none".|
|`width`|No|-|Custom width of the image (e.g. "100px", "100%").|
|`height`|No|-|Custom height of the image (e.g. "100px", "100%").|

|Property|Requi|red<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`aspect`<br>`Ratio`|No|-|Custom aspect ratio of the image (e.g. "16/9", "1").|
|`rounded`<br>`Corners`|No|`false`|Whether to apply Material Design standard rounded corners.|
|`border`|No|-|Custom border radius of the image (e.g. "50%", "12px").|
|`Radius`|||Overrides roundedCorners.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialImage",
   "url": "https://www.gstatic.com/marketing-
cms/assets/images/c5/3a/200414104c669203c62270f7884f/google-wordmarks-
2x.webp=n-w100-h32-fcrop64=1,00000000ffffffff-rw",
   "width": "100px",
   "height": "32px",
   "fit": "scaleDown",
   "roundedCorners": true,
   "alt": "Google Wordmark"
 }
]
```

#### MaterialProgressBar

A2UI wrapper for the Angular Material Progress Bar component. Supports determinate, indeterminate, buffer, and query modes. 

The following table outlines the properties available for the `MaterialProgressBar` component: 

|Property|Requi|red<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`value`|No|`0`|The progress value (0 to 100) in determinate and buffer<br>modes.|
|`mode`|No|`determin`<br>`ate`|The mode of the progress bar. One of: "determinate",<br>"indeterminate", "buffer", "query".|
|`buffer`<br>`Value`|No|`0`|The buffer value (0 to 100) in buffer mode.|
|`color`|No|-|Color palette of the progress bar ("primary", "accent", "warn").|
|`ariaLabel`|No|-|Discernible text for screen readers. Recommended for<br>accessibility when no visible label is present.|
|`aria`<br>`Labelledby`|No|-|Identifies the element (or elements) that labels the current<br>element. Used for accessibility.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialProgressBar",
   "mode": "determinate",
   "value": 75,
   "bufferValue": 90,
   "color": "primary",
   "ariaLabel": "Loading progress"
 }
]
```

#### MaterialProgressSpinner

A2UI wrapper for the Angular Material Progress Spinner component. Supports determinate and indeterminate modes, and custom dimensions. 

The following table outlines the properties available for the `MaterialProgressSpinner` component: 

|Property|Requi|red<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`value`|No|`0`|The progress value (0 to 100) in determinate mode.|
|`mode`|No|`determin`<br>`ate`|The mode of the spinner. One of: "determinate",<br>"indeterminate".|
|`diameter`|No|`40`|The diameter of the progress spinner in pixels.|
|`stroke`<br>`Width`|No|`4`|The width of the spinner stroke in pixels.|
|`color`|No|-|Color palette of the spinner ("primary", "accent", "warn").|
|`ariaLabel`|No|-|Discernible text for screen readers. Recommended for<br>accessibility when no visible label is present.|
|`aria`<br>`Labelledby`|No|-|Identifies the element (or elements) that labels the current<br>element. Used for accessibility.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialProgressSpinner",
   "mode": "indeterminate",
   "diameter": 40,
   "strokeWidth": 4,
   "color": "accent",
   "ariaLabel": "Loading data"
 }
]
```

#### MaterialTable

A2UI wrapper for the Angular Material Table component. Renders structured data into columns and rows. 

The following table outlines the properties available for the `MaterialTable` component: 

|Property|Requir|ed<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`columns`|Yes|-|An array of column definitions, each specifying a {header,<br>field} object.|
|`rows`|Yes|-|The list of data rows. Can be an array of key-value records or a<br>data binding reference.|
|`ariaLabel`|No|-|Discernible text for screen readers. Recommended for<br>accessibility when no visible label is present.|
|`aria`<br>`Labelledby`|No|-|Identifies the element (or elements) that labels the current<br>element. Used for accessibility.|
|`caption`|No|-|An accessible caption/description for the table.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialTable",
   "columns": [
     {
       "header": "ID",
       "field": "id"
     },
     {
       "header": "Name",
       "field": "name"
     },
     {
       "header": "Role",
       "field": "role"
```

<!-- Start of picture text -->
     }<br>   ],<br>   "rows": {<br>     "path": "/company/users"<br>   }<br> }<br>]<br><!-- End of picture text -->

#### MaterialText

Displays text with Material typography. 

The following table outlines the properties available for the `MaterialText` component: 

|Property|Requir|ed<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`text`|Yes|-|The text to be displayed. This can be a literal string or a reference<br>to a value in the data model.|
|`usage`|No|`body`|A hint for the typography style. One of: "h1", "h2", "h3", "h4",|
|`Hint`|||"h5", "subtitle1", "subtitle2", "body1", "body2", "body", "caption".|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|

<!-- Start of picture text -->
[<br> {<br>   "id": "root",<br>   "component": "MaterialText",<br>   "text": "Headline Large (H1)",<br>   "usageHint": "h1"<br> }<br>]<br><!-- End of picture text -->

### Material catalog navigation components

Navigation and action components allow users to perform actions or navigate between views. 

#### MaterialButton

Material Design button. 

The following table outlines the properties available for the `MaterialButton` component: 

|Property|Requi|red<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`label`|No|-|The text label to display on the button.|
|`leading`<br>`Icon`|No|-|The name of the Material Icon to display before the label.|
|`trailing`<br>`Icon`|No|-|The name of the Material Icon to display after the label.|
|`variant`|No|`basic`|The button style variant. One of: "raised", "flat", "stroked",<br>"icon", "fab", "mini-fab", "basic".|
|`appearance`|No|-|The visual appearance of the button. One of: "text", "filled",<br>"elevated", "outlined", "tonal".|
|`disabled`|No|`false`|Whether the button is disabled.|
|`action`|No|-|The action to be dispatched when the button is clicked.|
|`tooltip`|No|-|Tooltip text to display on hover.|
|`ariaLabel`|No|-|Discernible text for screen readers. Recommended for<br>accessibility when no visible label is present.|
|`disable`<br>`Ripple`|No|`false`|Whether the ripple effect on click is disabled.|
|`extended`|No|`false`|Whether the button is extended with additional label or icon<br>space.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialButton",
   "label": "Raised Button",
   "variant": "raised",
   "tooltip": "Click me!",
   "action": {
     "event": {
       "name": "click"
     }
   }
 }
]
```

#### MaterialIconButton

Material Design icon button. 

The following table outlines the properties available for the `MaterialIconButton` component: 

|Property|Requir|ed<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`icon`|Yes|-|The name of the Material Icon to display.|
|`action`|Yes|-|The client-side action to be dispatched when the icon button<br>is clicked.|
|`ariaLabel`|Yes|-|Discernible text for screen readers. Recommended for<br>accessibility since the button only contains an icon.|
|`aria`<br>`Labelledby`|No|-|Identifies the element (or elements) that labels the current<br>element. Used for accessibility.|
|`aria`<br>`Describedby`|No|-|Identifies the element (or elements) that describes the current<br>element. Used for accessibility.|
|`color`|No|-|Color palette of the button (primary, accent, warn).|

|Property|Requi|red<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`disabled`|No|`false`|Whether the button is disabled.|
|`tooltip`|No|-|Tooltip text to display on hover.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialIconButton",
   "icon": "favorite",
   "ariaLabel": "Favorite",
   "color": "warn",
   "action": {
     "event": {
       "name": "click"
     }
   }
 }
]
```

#### MaterialMenu

A2UI wrapper for the Angular Material Menu component. Provides a trigger button and drop-down menu items. 

The following table outlines the properties available for the `MaterialMenu` component: 

|Property|Requi|red<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`label`|No|-|The text label displayed on the menu trigger button.|
|`icon`|No|-|The name of the Material Icon to display on the trigger button.|

|Property|Requir|ed<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`disabled`|No|`false`|Whether the menu trigger button is disabled.|
|`value`|No|-|The currently selected value. Can be a literal string or a data<br>binding reference.|
|`options`|Yes|-|The list of menu options available. Can be an array of {label,<br>value} objects or a data binding reference.|
|`action`|No|-|The client-side action to be dispatched when a menu item is<br>selected.|
|`ariaLabel`|No|-|Discernible text for screen readers. Recommended for<br>accessibility when no visible label is present.|
|`aria`<br>`Labelledby`|No|-|Identifies the element (or elements) that labels the current<br>element. Used for accessibility.|
|`aria`<br>`Describedb`|`y`<br>No|-|Identifies the element (or elements) that describes the current<br>element. Used for accessibility.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialMenu",
   "label": "Options",
   "icon": "more_vert",
   "value": {
     "path": "/menu/selectedOption"
   },
   "options": [
     {
       "label": "Settings",
       "value": "settings"
     },
     {
       "label": "Help",
       "value": "help"
```

<!-- Start of picture text -->
     },<br>     {<br>       "label": "Logout",<br>       "value": "logout"<br>     }<br>   ],<br>   "action": {<br>     "event": {<br>       "name": "menuSelection"<br>     }<br>   }<br> }<br>]<br><!-- End of picture text -->

#### MaterialTabs

A2UI wrapper for the Angular Material Tabs component. Renders tabbed navigation and manages active tab selection. 

The following table outlines the properties available for the `MaterialTabs` component: 

|Property|Requir|ed<sup>Default</sup><br>Value|Description|
|---|---|---|---|
|`tabs`|Yes|-|An array of tab definitions, each specifying a {label, content}<br>object.|
|`activeTab`|No|`0`|The 0-based index of the currently active tab. Can be a literal<br>number or a data binding reference.|
|`ariaLabel`|No|-|Discernible text for screen readers. Recommended for<br>accessibility when no visible label is present.|
|`aria`<br>`Labelledby`|No|-|Identifies the element (or elements) that labels the current<br>element. Used for accessibility.|
|`style`|No|-|Inline styles to apply to the element.|
|`weight`|No|-|Layout weight for the element when placed in a flex container.|

```
[
 {
   "id": "root",
   "component": "MaterialTabs",
   "activeTab": {
     "path": "/app/selectedTab"
   },
   "tabs": [
     {
       "label": "Overview",
       "content": "Overview content"
     },
     {
       "label": "Details",
       "content": "Details content"
     },
     {
       "label": "Reviews",
       "content": "Reviews content"
     }
   ]
 }
]
```
